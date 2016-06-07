import itertools
import urllib.request

#grabs the info from www.google.com/Finance anything inside of SnapDate has all of the information.
#Including generic information about the company
def grabMetaInfo():
	#using SnapDate

#Once the data is collected in grabMetaInfo() it needs to be sorted into correct categories in the mySQL Database.
def sortMetaData():

#Grabs the URL and encodes it to UTF-8
def grabURL(quote):
        req = urllib.request.Request('http://www.google.com/finance?q={}'.format(quote))
        response = urllib.request.urlopen(req)
        the_page = response.read()
        new_page = str(the_page, encoding='UTF-8')
        return new_page
