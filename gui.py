import tkinter as tk

#calling a action when button is clicked
def some_function():
    print("works")

#creating a root
root = tk.Tk()

#label 
label = tk.Label(root, text= "Library")
label.pack()

#button
button = tk.Button(root, text="Button", command=some_function)
button.pack()

#to run the gui
root.mainloop() 