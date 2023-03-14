import csv

books=[["Name","ISBN"]]
while True:
    bookName=input("Book Name: ")
    if bookName=="false":
        break
    bookISBN=input("Book ISBN: ")
    book=[bookName,bookISBN]
    books.append(book)
with open('bookList.csv', 'w', newline='') as file: 
    writer=csv.writer(file)
    writer.writerows(books)