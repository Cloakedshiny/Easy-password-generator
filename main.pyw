import random
import secrets
import string
import tkinter
import tkinter as tk
from tkinter import *

root = Tk()
root.title("Password generator :)")
root.resizable(height=FALSE,width=FALSE)

passframe = tkinter.Text(root,relief=GROOVE)

def generate8():
     password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(8))
     passframe.insert('1.0',password+'\n')

def generate10():
     password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(10))
     passframe.insert('1.0',password+'\n')

def generate16():
     password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(16))
     passframe.insert('1.0',password+'\n')

generatebutton1 = tk.Button(text="Generate a password (16 Characters)",relief=GROOVE,command=generate16)
generatebutton2 = tk.Button(text="Generate a password (10 Characters)",relief=GROOVE,command=generate10)
generatebutton3 = tk.Button(text="Generate a password (8 Characters)  ",relief=GROOVE,command=generate8)

root.geometry("350x385")
generatebutton1.pack(expand=TRUE)
generatebutton2.pack(expand=TRUE)
generatebutton3.pack(expand=TRUE)
passframe.pack(expand=TRUE)
root.mainloop()
