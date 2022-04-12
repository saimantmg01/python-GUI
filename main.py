# make library
library = {}
# name shelf
shelf = input("name this shelf: ")

#space for shelf
library[shelf] = []
#space for book, description and author
library[shelf].append([])
book = input("put a book here: ")
description = input("put a description: ")
author = input("put a Author: ")
library[shelf][0].append(book)
library[shelf][0].append(description)
library[shelf][0].append(author)
#  NOTE: shelf is a string NOT an index
# a for loop to keep doing this key would be 0, 1, ect.
library[shelf].append([])
book = input("put a book here: ")
description = input("put a description: ")
Author = input("put a Author: ")
library[shelf][1].append(book)
library[shelf][1].append(description)
library[shelf][1].append(author)

#for loop here if you want

print(library)
# how to grab the description of book 2
print(library['shelf'][1][1])
# how to grab the author of book 1
print(library['shelf'][0][2])

# library['shelf'] -> {[book1... dic1...],[],[]....} everything in shelf
# library['shelf'][0] -> book1... dic1... book1's stuff
# library['shelf'][0][0] -> just the name of book1
