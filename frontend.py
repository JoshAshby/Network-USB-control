#!/usr/bin/env python
#import all needed libraries
from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import sys
import backstage
root = Tk()

def close():
    exit(0)
    
def send():
    data = text.get()
    text.delete(0, END)
    backstage.send(data)

def recieve():
    data = backstage.recieve()
    textin["text"] = data

if (len(sys.argv) > 1):
    fn = sys.argv[1]

toolbar = Frame(root)#create the tool bar
main = Frame(root)#create the main text area

bu = Button(toolbar, text="Send", width=6, command=send, fg ="green", bg ="black",)#close button
bu.grid(column = 0, row = 0, padx=2, pady=2)

bu = Button(toolbar, text="Close", width=6, command=close, fg ="green", bg ="black",)#close button
bu.grid(column = 1, row = 0, padx=2, pady=2)

bu = Button(toolbar, text="Recieve", width=6, command=recieve, fg ="green", bg ="black",)#get data
bu.grid(column = 2, row = 0, padx=2, pady=2)

toolbar.grid(column = 0, row = 0)#place the toolbar on a grid cell
main.grid(column = 0, row = 1)#place the text area on a grid cell

text = Entry(main, background = "black", foreground="green")#make the text area
text.grid(column = 0, row = 1, padx = 2, pady = 2)
text.focus()#set focus on the textbox when the program starts

textin = Label(main, background = "black", foreground = "green")
textin.grid(column = 0, row = 2, padx = 2, pady = 2)

mainloop()#loop the program