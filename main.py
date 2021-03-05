#! usr/bin/python3

from tkinter import *
import os
from PIL import ImageTk, Image

# init
master = Tk()
master.title('Banking App')

# image import
# img = Image.open('secure.png')
# img = img.resize((150, 150))
# img = Image.Tk.PhotoImage(img)

# foo
def register():
    register_screen = Toplevel(master)
    register_screen.title('Register')
    Label(register_screen, text='Please enter your details below', font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text='Name', font=('Calibri', 14)).grid(row=1, sticky=W)
    Label(register_screen, text='Email', font=('Calibri', 14)).grid(row=2, sticky=W)
    Label(register_screen, text='Age', font=('Calibri', 14)).grid(row=3, sticky=W)
    Label(register_screen, text='Password', font=('Calibri', 14)).grid(row=4, sticky=W)
    
    Entry(register_screen).grid(row=1, column=0)

    
    
def login():
    print("Welcome to the Login page.")

# labels
Label(master, text='Banking App', font=('Calibri', 20)).grid(row=0, sticky=N, pady=10)
Label(master, text='Creator: Adrian B.', font=('Calibri', 12)).grid(row=1, sticky=N)

# buttons
Button(master, text='Register', font=('Calibri', 12), width=10, command=register).grid(row=3, sticky=N, pady=5)
Button(master, text='Login', font=('Calibri', 12), width=10, command=login).grid(row=3, sticky=N, pady=30)


master.mainloop()

# Fix grid TODO