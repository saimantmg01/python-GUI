import csv
import tkinter as tk
from parser_file import csv_reader

#creating a root window
window = tk.Tk()

#functions
#calling a action when button is clicked
def display():
    #library = {'shelf1': {'Curious George': ['monkey', 'Christopher'], 'Henry and Mudge': ['About a boy and his dog', 'Bob'], 'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 'Bone': ['human bones', 'Michelle']}}
    
    library = csv_reader()
    greeting = f'Hello {str(entry_field1.get())}'

    #create a text field
    greeting_display = tk.Text(master= window, height=100, width = 100)
    greeting_display.pack()
    greeting_display.insert(tk.END,"{} \n This is what we currently have in our library dictionary : \n {}".format(greeting, library))

#title of window
window.title("Library GUI")

#size of window
window.geometry("500x500")

#adding a background image
background_image = tk.PhotoImage(file='library.png')
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

#label 
title = tk.Label(window, text= "Welcome to our library!!!!")
title.pack()

#testing
label1 = tk.Label(window, text="Testing: See all the book in library!!!")
label1.pack()

label2 = tk.Label(window, text="What is your name?")
label2.pack()

#entry field - blank box where you can type anything
entry_field1 = tk.Entry(window)
entry_field1.pack()


#button
button = tk.Button(window, text="Click me", command=display)
button.pack()

#to run the gui
window.mainloop() 