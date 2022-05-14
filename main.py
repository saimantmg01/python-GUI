import csv
# Code here
# Open a file for writing
with open('./test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
library = {}
# what the user has
hand = {}
# a place to put books in for organization and convenient
box = []
#make the shelf
shelf = 'shelf1'
library[shelf] = {}
for n in range(-1, len(data[0])):
    book = data[n][0]
    # Space for author and description
    library[shelf][book] = []
    library[shelf][book].append(data[n][1])
    library[shelf][book].append(data[n][2])
#^
#|
# to make another shelf you need to do this process again

# user input for taking out book
def take_out():
    if len(library[shelf]) == 0:
        print("There aren't any books left")
        main()
    keep_going = 'y'
    while keep_going == 'y':
        x = 1
        print('Choose a book to take out')
        for key in library[shelf]:
            print(f"{x}. {key}")
            x = x + 1
            box.append(key)
        x = x - 1
        i = int(input())
        while i > x or i < 1:
            print("That is not a choice")
            i = int(input())      
        i = i-1
        print(f"You chose, {box[i]}")
        # author
        print(f"by {library[shelf][box[i]][0]}")
        # description
        print(f"it is about {library[shelf][box[i]][1]}")
        book = box[i]
        hand[book] = []
        hand[book].append(library[shelf][box[i]][0])
        hand[book].append(library[shelf][box[i]][1])
        print("You have")
        print(hand)
        del library[shelf][box[i]]
        box.clear()
        # check if the library shelf is empty
        if len(library[shelf]) == 0:
            print("There aren't any books left")
            break
        keep_going = input('Do you want to take out another book yes = y or no = n: ')
        if keep_going == 'n':
            break
 
# user input for putting in book   
def put_in():
    if len(hand) == 0:
        print("You don't have any books")
        main()
    keep_going = 'y'
    while keep_going == 'y':
        x = 1
        print('Choose a book to put back')
        for key in hand:
            print(f"{x}. {key}")
            x = x + 1
            box.append(key)
        x = x - 1
        i = int(input())
        while i > x or i < 1:
            print("That is not a choice")
            i = int(input())      
        i = i-1
        book = box[i]
        library[shelf][book] = []
        library[shelf][book].append(hand[book][0])
        library[shelf][book].append(hand[book][1])
        print(library)
        del hand[box[i]]
        box.clear()
        if len(hand) == 0:
            print("You don't have any books")
            main()
        keep_going = input('Do you want to put in another book yes = y or no = n: ')
        if keep_going == 'n':
            break

#gives position of book in list for review functions
def find_book(name, list):
    for n, item in enumerate(list):
        if item[0] == name:
            return n
        
#add inputted reviews to a book in the csv 
def add_review(book,review):
    l = []
    with open("test.csv") as f:
        for i in f:
            l.append(i.split(','))
    book = find_book(book,l)
    if len(l[book]) < 4:
        l[book].append(review + '\n')
        l[book][2] = l[book][2].replace('\n','')
    else:
        l[book][3] = l[book][3].replace('\n','') + f'|{review}' + '\n'
    print(l)
    print(find_book("Bone",l))
    print(l)
    with open("test.csv",'w') as f:
        for i in l:
            f.write(','.join(i))

#get the reviews for a current book - returns a list
def get_reviews(book):
    l = []
    with open("test.csv") as f:
        for i in f:
            l.append(i.split(','))
    info = l[find_book(book,l)]
    if len(info) < 4:
        return ''
    return info[3].split('|')

#removes all reviews from a book
def clear_reviews(book):
    l = []
    with open("test.csv") as f:
        for i in f:
            l.append(i.split(','))
    if len(l[find_book(book,l)]) > 3:
        l[find_book(book,l)] = l[find_book(book,l)][:3]
        l[find_book(book,l)][2] += '\n'
    with open("test.csv",'w') as f:
        for i in l:
            f.write(','.join(i))


def main():
    do_something = 0
    while do_something != 3:
        do_something = int(input("""What do you want to do 
                                1. Take out a book 
                                2. Put in a book 
                                3. Leave
                                """))
        if do_something == 1:
            take_out()
        elif do_something == 2:
            put_in()
    if do_something == 3:
        print("Thanks for visiting the library")
        quit()
# main()
# library['shelf'] -> {[book1... dic1...],[],[]....} everything in shelf
# library['shelf'][0] -> book1... dic1... book1's stuff
# library['shelf'][0][0] -> just the name of book1
# test here type somthing