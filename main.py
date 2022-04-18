# Make the library
library = {}
#######################################
# Name shelf
shelf = input("name this shelf: ")
# Space for book
library[shelf] = {}
book = input("name this book: ")
# Space for description and author
library[shelf][book] = []
d = input("description for book: ")
a = input("Author for book: ")
library[shelf][book].append(d)
library[shelf][book].append(a)

# assume 'a' was your shelf name
# print(library['a'][book][0])
# print(library['a'][book][1])
#######################################
#^
#|
# to make another shelf you need to do this process again


#for loop here if you want


# library['shelf'] -> {[book1... dic1...],[],[]....} everything in shelf
# library['shelf'][0] -> book1... dic1... book1's stuff
# library['shelf'][0][0] -> just the name of book1
