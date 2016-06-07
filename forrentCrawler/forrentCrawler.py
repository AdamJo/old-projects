import json
import requests
import re 
from bs4 import BeautifulSoup
import psycopg2
import time
from datetime import datetime

SITES_TO_SEARCH = {
    'forrent' : 'http://www.forrent.com/',  #ForRent, Apartments
    'zillow' : 'http://www.zillow.com/', #Zillow, House / Apartments
}

CITY = 'Omaha'
STATE = 'NE'

def check_site_status_code():
    """Check if websites are still available
    """
    print ('Check to see if sites are still sending <Response [200]>')
    for name, website in SITES_TO_SEARCH.items():
        status_request = requests.get(website).status_code 
        if requests.get(website).status_code == 200:
            print ("OK")
        else:
            print ('EH?')

def search_save_robots():
    """grabs and saves robots.txt to disk
    """
    for name, website in SITES_TO_SEARCH.items():
         with open('robot_check\%s_robot.txt' % name, 'w') as fle:
            robot_request = requests.get(website+'robots.txt')
            fle.write(robot_request.text)

def soup_to_text(soup):
    """takes in a list of soup tags from find_all and returns a list of the text
    """
    return [single_tag.getText() for single_tag in soup]

def len_variable_check(*args):
    """Checks length of each selection to see if it matches with 
    """
    for argument in args:
        print (len(argument))

def max_pages(url):
    """Determines the max number of pages for the given area.
    """
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data)
    page_number = (soup_to_text(soup.select('div[class="unitRt"] > a')))
    page = list()
    for x in page_number:
        if x.isdigit():
            page.append(int(x))
    return (max(page))

def none_check(list_check, count_check):
    """used to create replace bad entries with a #.
    try:
        return list_check[count_check]
    except:
        return '#'

def forrent_pull_data():
    """Crawls through forrent.com and grabs the needed data.
    """
    website = SITES_TO_SEARCH['forrent']
    url = website+'find/NE/metro-Omaha/Omaha/show-40'
    max_page = max_pages(url)

    for page in range(max_page):
        response = requests.get('%s/page-%s' % (url, page+1))
        data = response.text
    
        soup = BeautifulSoup(data)

        apartment_names = soup_to_text(soup.select('h2 > a'))
        street_address = soup_to_text(soup.find_all('span', 'street-address'))
        zip_code = soup_to_text(soup.find_all('span', class_='postal-code mr5'))
        phone_number = soup_to_text(soup.find_all(href=re.compile(r'tel:\+[\d-]+')))

        regex = re.compile(r'\n+([1|2|3]? ?[a-zA-Z]+)\n+From\n+\$?([0-9a-zA-Z! ]+)')
        prices_of_apartment = soup_to_text(soup.find_all('ul', 'line gutters sep'))
        prices_of_apartment = [ re.findall(regex, apartment) for apartment in prices_of_apartment ]

        postal_code = list()
        for count in range(len(apartment_names)):
            postal_code.append('%s, %s, %s, %s %s' % (none_check(apartment_names, count), none_check(street_address, count), CITY, STATE, none_check(zip_code, count)))

        link = [ a_tag.attrs['href'] for a_tag in soup.select('h2 > a') ]

        lat_long = soup_to_text(soup.find_all('div', 'geo hide'))
        latitude = list()
        longitude = list()
        for coordinates in lat_long:
            temp_cord = ((list(filter(None, coordinates.split('\n')))))
            latitude.append(temp_cord[0])
            longitude.append(temp_cord[1])

        database_data = list()

        for count in range(len(apartment_names)):
            database_data.append({
                'apartment_name' : none_check(apartment_names, count).strip(), 
                'street_address' : none_check(street_address, count).strip(),
                'city' : 'Omaha',
                'state' : 'NE',
                'zip_code' : none_check(zip_code, count).strip(),
                'postal_address' : postal_code[count].strip(),
                'phone_number' : none_check(phone_number, count).strip(),
                'link' : none_check(link, count).strip(),
                'latitude' : none_check(latitude, count).strip(),
                'longitude' : none_check(longitude, count).strip(),
                'prices' : none_check(prices_of_apartment, count)
            })
        export_to_database(database_data)

def export_to_database(all_data):
        """pushes data to postgresql database
        """
        connection = psycopg2.connect(database='rentCrawler', user='postgres', port='5433')
        cursor = connection.cursor()

        cursor.executemany("""INSERT INTO forrent( \
            apartment_name, street_address, city, state, zip_code, postal_address, phone_number, link, latitude, longitude) \
            SELECT %(apartment_name)s, %(street_address)s, %(city)s, %(state)s, %(zip_code)s, \
             %(postal_address)s, %(phone_number)s, %(link)s, %(latitude)s, %(longitude)s \
            WHERE NOT EXISTS (SELECT apartment_name FROM forrent WHERE apartment_name = %(apartment_name)s)""", all_data)

        for count in range(len(all_data)):
            for apartment_layouts in all_data[count]['prices']:
                try:
                    cursor.execute("""INSERT INTO forrent_prices (apartment_name, layout, price) \
                        VALUES (%(name)s, %(layout)s, %(price)s);""", { 'name' : all_data[count]['apartment_name'], 'layout' : apartment_layouts[0], 'price' : apartment_layouts[1]})
                except:
                    print ('apartment does not have price value')

        connection.commit()
        if connection:
            connection.close()

if '__main__' == __name__:
    forrent_pull_data()