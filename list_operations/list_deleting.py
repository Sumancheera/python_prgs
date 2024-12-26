books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
read_books = []
read = books.pop(0)
read_books.append(read)
# read_books
# ['Dragonsbane']
# books
# ['The Hobbit', 'Wonder', 'Jaws']
print(read_books)
##   ## del list[index]
    ##                  ###
books = ["Dragonsbane","The Hobbit","Wonder","Wonder","Jaws","Jaws"]
del books[2] #index
print(books)
# books
# ['Dragonsbane', 'The Hobbit', 'Wonder', 'Jaws', 'Jaws']
del books[-1]
print(books)
del books[0:3] #del books[-3:-1]
print(books) 