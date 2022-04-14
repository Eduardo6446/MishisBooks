import string
import requests
import json


#bookName = input("Enter Book Name: ")

isbn='0425285049'
response = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn).json()

book = response['items'][0]['volumeInfo']['averageRating']
book2 = response['items'][0]['volumeInfo']['ratingsCount']
des = response['items'][0]['volumeInfo']['description']
cat = response['items'][0]['volumeInfo']['categories']
imagen = response['items'][0]['volumeInfo']['imageLinks']['thumbnail']


#count = book.get('ratingsCount')
#rating = book.get('average_rating')
print(book)
print(book2)
print(des)
print(cat)
print(imagen)

#book = book + 2
#print(book)
#book2 = book2 + 2
#print(book2)
#result = requests.get("https://www.googleapis.com/books/v1/volumes?q=" + bookName)

#book = result.json()

#items = book['items']

#encoded = json.dumps(items)
#decoded = json.loads(encoded)

#print(decoded[0]['volumeInfo']['infoLink'])