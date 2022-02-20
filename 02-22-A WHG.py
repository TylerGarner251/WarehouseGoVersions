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
root.geometry("920x480")
root.resizable(width=0, height=0)
root.configure(bg=defaultBackground)

##__Displaying on the window__##
# title label,
# colour of the background label
# lable text font and colour
# packs label to work
displayedMessage = tk.Label(text="WarehouseGo",font=("Courier", 20, "bold"),fg = ("white"),bg=defaultBackground)
displayedMessage.grid(row=0, column=0)

##__Creating entry box to display__##
# Entry box font and text
productEntry = Entry(root,font=("Courier", 12), border = 3)
productEntry.grid(row=1, column=0, padx = 5, pady = 5)

##__Grabbing Product Files__##
# gets directory
path = 'C:\\Users\\tyler\\Downloads\\resources'
productFile = os.listdir(path)

##__Creating List box to display__##
# creates shape and visual of the list box
listbox = tk.Listbox(root,height = 10, width = 30, border = 3)
listbox.grid(row=3, column=0, pady = 10)

##__fillouts the listbox__##
def fillout(event):
    productEntry.delete(0, END)
    productEntry.insert(0, listbox.get(ANCHOR))

##__narrows down the listbox from entry search__##
# grabs the entrybox
# puts characters in list and compares to listbox
def scankey(event):
    val = event.widget.get()
    
    if val == "":
        data = productFile
    else:
        data = []
        for item in productFile:
            if val.upper() in item.upper():
                data.append(item)
    update(data)

def update(data):
    listbox.delete(0, "end")
    for item in data:
        listbox.insert("end", item)

# Delete Function
#def delete():
    #deleteEntry = productEntry.get()
    #str(deleteEntry)
    #listbox.delete(ANCHOR)
    #os.remove(path + "\\" + deleteEntry)
    #root.destroy()

# Delete button
#deleteButton =  Button(root, text="Delete", command=delete)
#deleteButton.pack(pady=10)

#__listbox bind__#
listbox.bind("<<ListboxSelect>>", fillout)
#__Entry search bind__#
productEntry.bind("<KeyRelease>", scankey)

update(productFile)  # Add the items in to the listbox
root.mainloop()
