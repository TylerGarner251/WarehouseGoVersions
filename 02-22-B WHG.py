import unittest
import tkinter as tk
from tkinter import *
import sys
import os
import time
##__Background options__##
defaultBackground = "#2D2D2D"
LightMode = "light grey"

##__creating window as root__##
# creates title,
# size of the window, 
# stops window resize, 
# colour of background
root = Tk()
root.title('WarehouseGo')

class App(Frame):

    root.geometry("920x480")
    root.resizable(width=0, height=0)
    root.configure(bg=defaultBackground)
    root.grid_rowconfigure(1, weight=1)

    ##__Creating entry box to display__##
    # Entry box font and text
    productEntry = Entry(root,font=("Courier", 12), border = 3)
    productEntry.grid(row=2, column=0, padx = 5, pady = 5)

    ##__Grabbing Product Files__##
    # gets directory
    def directory(self):
        self.path = 'C:\\Users\\tyler\\Downloads\\resources'
        self.productFile = os.listdir(self.path)

    ##__Creating List box to display__##
    # creates shape and visual of the list box
    listbox = tk.Listbox(root,height = 5, width = 31, border = 3)
    listbox.grid(row=3, column=0, padx = 2, pady = 5)

    ##__fillouts the listbox__##
    def fillout(self,event):
        self.productEntry.delete(0, END)
        self.productEntry.insert(0, self.listbox.get(ANCHOR))

    ##__narrows down the listbox from entry search__##
    # grabs the entrybox
    # puts characters in list and compares to listbox
    def scankey(self,event):
        val = event.widget.get()
    
        if val == "":
            data = self.productFile
        else:
            data = []
            for item in self.productFile:
                if val.upper() in item.upper():
                    data.append(item)
        self.update(data)
 
    def update(self,data):
        self.listbox.delete(0, "end")
        for item in data:
            self.listbox.insert("end", item)


    # Delete Function
    def delete(self):
        deleteEntry = self.productEntry.get()
        str(deleteEntry)
        self.listbox.delete(ANCHOR)
        os.remove(self.path + "\\" + deleteEntry)

    # Delete button
    deleteButton =  Button(root, text="Delete", command=delete)
    deleteButton.grid(row=3, column=2, padx = 5, pady = 5)

    #__listbox bind__#
    listbox.bind("<<ListboxSelect>>", fillout)
    #__Entry search bind__#
    productEntry.bind("<KeyRelease>", scankey)

    update(directory.productFile)  # Add the items in to the listbox

App.root.mainloop()