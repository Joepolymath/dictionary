from tkinter import *
import os
from os import sys

def shutdown():
    os.system('shutdown /s')

def hibernate():
    os.system('shutdown /h')

def signout():
    os.system('shutdown /l')

def restart():
    os.system('shutdown /r')



wn = Tk()
wn.title("ShuTle")
wn.geometry("400x400")


can = Canvas(wn, width=400, height=400, bg="#1790C9")
can.pack()

frm = Frame(can, bg = 'white')
frm.place(relwidth = 0.9, relheight = 0.8, relx = 0.05, rely=0.1)

home = Label(frm, text = "ShuTool", bg = 'white', fg='black')
home.config(font = ('jokerman 15'))
home.place(relx = 0.4, rely=0.002)

# the signout button
sign = Button(frm, text = "SignOut", width = 10, height = 3, relief = FLAT, command = signout)
sign.place(relx = 0.1, rely=0.3)

#hibernate button
hib = Button(frm, text = "Hibernate", width = 10, height = 3, relief = FLAT, command = hibernate)
hib.place(relx = 0.68, rely=0.3)

#restart button
res = Button(frm, text = "Restart", width = 10, height = 3, relief = FLAT, command = restart)
res.place(relx = 0.39, rely=0.52)


# shutdown button
shut = Button(frm, text = "ShutDown", width = 10, height = 3, relief = FLAT, command = shutdown)
shut.place(relx = 0.39, rely=0.75)




wn.mainloop()