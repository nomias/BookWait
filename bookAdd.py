import csv
from book import Book

books=[]
while True:
    bookName=input("Book Name: ")
    if bookName=="false":
        break
    bookISBN=input("Book ISBN: ")
    book=Book(bookName,bookISBN)
    books.append(book)
book=books[0]
print(book)
fields=["Name","ISBN"]
with open('bookList.csv', 'w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()
    #for book in books:
     #   writer.writerow(book)
#f=open("bookList.csv","w")