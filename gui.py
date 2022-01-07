import tkinter as tk
from tkinter import *
import random
import string
import os.path


window = Tk()

name_var = tk.StringVar()

length_var = tk.IntVar()

numDig_var = tk.IntVar()

numSpec_var = tk.IntVar()

#ui layout

name_label = Label(window, text="What is this password for?", font=("calibre", 10, "bold"))
name_label.grid(row = 0, column = 0)
name_entry = Entry(window, textvariable=name_var, font=("calibre", 10, "normal"))
name_entry.grid(row=0, column=1)

length_label = Label(window, text="Password length:", font=("calibre", 10, "bold"))
length_label.grid(row=1, column=0)
length_entry = Entry(window, textvariable=length_var, font=("calibre", 10, "normal"))
length_entry.grid(row=1, column=1)



numDig_label = Label(window, text="Number of digits:", font=("calibre", 10, "bold"))
numDig_label.grid(row=2, column=0)
numDig_Entry = Entry(window, textvariable=numDig_var, font=("calibre", 10, "normal"))
numDig_Entry.grid(row=2, column=1)


numSpec_label = Label(window, text="Number of special characters:", font=("calibre", 10, "bold"))
numSpec_label.grid(row=3, column=0)
numSpec_Entry = Entry(window, textvariable=numSpec_var, font=("calibre", 10, "normal"))
numSpec_Entry.grid(row=3, column=1)

#password generation

def password_gen():
    numDig_var = int(numDig_Entry.get())
    numSpec_var = int(numSpec_Entry.get())
    name_var = name_entry.get()
    length_var = int(length_entry.get())

    filler = length_var - (numDig_var + numSpec_var)
    if (filler < 0):
        print("Number of specified characters exceeds total password length. Shutting down...")
        return
        pass
    caseMix = list(string.ascii_letters)

    password_tray = []

    for i in range(numDig_var):
        password_tray.append(random.choice(string.digits))

    for i in range(numSpec_var):
        password_tray.append(random.choice(string.punctuation))

    for i in range(filler):
        password_tray.append(random.choice(caseMix))

    password = ("".join(password_tray))
    passStore(password, name_var)
    success = Label(window, text="password created!", font=("calibre", 10, "bold"))
    success.grid(row=4, column=1)

#creates a text file if there isnt one already and stores the password in said text file

def passStore(password, name):
    storage_exists = os.path.exists('passwords.txt')

    if storage_exists == False:
        with open('passwords.txt', 'w') as c:
            c.write('Passwords: \n\n')
    with open('passwords.txt', 'a') as c:
        c.write("\n\n" + name + "\n")
        c.write(password)


submit = Button(window, text="Generate Password", command=password_gen)

submit.grid()

window.mainloop()

#this was so much more of a headache than it should've been