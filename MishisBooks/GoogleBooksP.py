import string
import requests
import json


#bookName = input("Enter Book Name: ")

isbn='080213825X'
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn).json()

book = response['items'][0]['volumeInfo']['averageRating']
book2 = response['items'][0]['volumeInfo']['ratingsCount']
libroImage = response['items'][0]['volumeInfo']['imageLinks']['thumbnail']
#count = book.get('ratingsCount')
#rating = book.get('average_rating')
print(book)
print(book2)
print(libroImage)
#result = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + bookName)

#book = result.json()

#items = book['items']

#encoded = json.dumps(items)
#decoded = json.loads(encoded)

#print(decoded[0]['volumeInfo']['infoLink'])