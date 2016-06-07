URL = 'http://www.paulgraham.com/articles.html' 
BASE_URL = 'http://www.paulgraham.com' 

def format_data(soup): 
    """takes in soup data to grab the title and url to search 
    """ 
    list_of_urls_titles = [] 
    for tag in soup: 
        list_of_urls_titles.append(['{}/{}'.format(BASE_URL, tag.attrs['href']), tag.getText()]) 
    return list_of_urls_titles 

def visible(element): 
    """Used to find only the text shown on the webpage when pulling from it
    Found on Stackoverflow 
    http://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text 
    """ 
    from re import match 
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']: 
        return False 
    elif match('<!--.*-->', str(element)): 
        return False 
    return True 

def sort_through_words(data): 
    """takes in a iterator and sorts each word into a Counter object
    """ 
    text = ' '.join([x for x in data]) 
    from re import findall 
    words =  (findall(r'[\w\']+', text.lower())) 
    from collections import Counter 
    return Counter(words) 

def main():
    from requests import get 
    response = get(URL) 

    from bs4 import BeautifulSoup 
    soup = BeautifulSoup(response.text) 
    list_urls_titles = format_data(soup.select('font > a')) 

    list_of_counters = [] 
    from collections import Counter 
    total_words = Counter() 
    for url, title in list_urls_titles: 
        soup = BeautifulSoup(get(url).text) 
        page = soup.findAll(text=True) 
        visible_text = filter(visible, page) 
        words_on_page = sort_through_words(visible_text) 
        list_of_counters.append(words_on_page) 
        total_words += words_on_page 

    print (total_words)

if __name__ == '__main__':
    main()