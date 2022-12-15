#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nandini
#
# Created:     15-12-2022
# Copyright:   (c) Nandini 2022
# Licence:     <your licence



from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('900x400')
tkWindow.title('login to nandinis app - hello cutiess')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=8, column=0)

tkWindow.mainloop()
