# make library
library = {}
# name shelf
shelf = input("name this shelf: ")

#space for shelf
library[shelf] = []
#space for book and description
library[shelf].append([])
book = input("put a book here: ")
description = input("put a description: ")
library[shelf][0].append(book)
library[shelf][0].append(description)
#  NOTE: shelf is a string NOT an index
# a for loop to keep doing this key would be 0, 1, ect.
library[shelf].append([])
book = input("put a book here: ")
description = input("put a description: ")
library[shelf][1].append(book)
library[shelf][1].append(description)

#for loop here if you want

print(library)
