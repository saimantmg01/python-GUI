import csv
start_time = time.time()
# Open a file for writing
with open('csv file name here', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
library = {}
#make the shelf
shelf = 'shelf1'
library[shelf] = {}
for n in range(-1, len(data[0])):
    ########################################
    # Space for book
    book = data[n][0]
    # Space for description and author
    library[shelf][book] = []
    description = data[n][1]
    author = data[n][2]
    library[shelf][book].append(description)
    library[shelf][book].append(author)
    #######################################
    #^
    #|
    # to make another shelf you need to do this process again

#######################################
# user input for book
box = []
x = 1
print('choose a book')
for key in library[shelf]:
    print(f"{x}. {key}")
    x = x + 1
    box.append(key)
x = x - 1
i = int(input())
while i > x or i < 1:
    print(" not a choice")
    i = int(input())      
i = i-1
print(f"You chose, {box[i]}")
# description
print(library[shelf][box[i]][0])
# author
print(f"by {library[shelf][box[i]][1]}")
#######################################
#! Find a way to pop a book from shelf

# library['shelf'] -> {[book1... dic1...],[],[]....} everything in shelf
# library['shelf'][0] -> book1... dic1... book1's stuff
# library['shelf'][0][0] -> just the name of book1
