import itertools
import urllib.request

#creates a list of quotes from 'a' to 'zzzzz'
def genQuotes():
	count = 0
	quotes = []
	outputFile = open("C:/ListOfQuotes(5).txt", "w")
	tupleQuotes = list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=2))
	for temp in tupleQuotes:
		genQuotes = ''.join(tupleQuotes[count])
		quotes.append(genQuotes)
		outputFile.write(genQuotes +'\n')
		count = count + 1
	return quotes

#identifies if the quote is valid or not if the webpage is less than 16000 characters than it is invalid.
def validQuote (quote):
    check = urllib.request.Request('http://money.cnn.com/quote/quote.html?symb={}'.format(quote))
    response = urllib.request.urlopen(check)
    the_page = response.read()
    new_page = str(the_page, encoding='latin-1')
    print ("{} = {}".format(quote, len(new_page)))
    if (len(new_page) < 40100):
    	return ("#Does not Exist = {}".format(quote))
    return quote
