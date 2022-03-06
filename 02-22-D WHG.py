import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image 
import sys
import os
import time

root = Tk()
root.title('WarehouseGo') # creates title,
class WarehouseGO(tk.Frame):
    def __init__(self,*args,**kwargs):
        tk.Frame.__init__(self,*args,**kwargs)
        ##__refreshing window fuction__##
        def refresh(self): # destroys window and then creates window
            self.destroy()
            self.__init__()

        ##__Refresh console__##
        def update(data):
            listbox.delete(0, "end")
            for item in data:
                listbox.insert("end", item)
        
        ##__Background options__##
        defaultBackground = "#2D2D2D"
        LightMode = "light grey"

        ##__creating window as root__##
        root.geometry("920x480") # size of the window
        root.resizable(width=0, height=0) # stops window resize
        root.configure(bg=LightMode) # colour of background
        root.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1) # column Configure grid system
        root.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1) # row configure grid sytstem

        ##__Creating entry box to display__##
        # Entry box font and text
        productEntry = Entry(root,font=("Courier", 12), border = 3)
        productEntry.grid(row=7, column=0, sticky='SW', padx = 10, pady = 5)

        ##__Grabbing Product Files__##
        # gets directory
        for i in range(0,100):
            while True:
                try: # tries to find the file locaiton
                    path = 'C:\\Users\\tyler\\OneDrive - Canterbury Christ Church University\\Documents\\Uni Work\\Delvelopment project\\WarehouseGO\\WarehouseGO\\Resources'
                    productFile = os.listdir(path)
                except: # if try fails to creates resources folder and retries try
                    directory = "Resources"
                    parent_dir = "C:\\Users\\tyler\\OneDrive - Canterbury Christ Church University\\Documents\\Uni Work\\Delvelopment project\\WarehouseGO\\WarehouseGO"
                    creatingDir = os.path.join(parent_dir, directory)
                    os.mkdir(creatingDir)
                    continue
                break

        ##__Creating List box to display__##
        # creates shape and visual of the list box
        listbox = tk.Listbox(root,height = 5, width = 33, border = 3)
        listbox.grid(row=8, column=0, sticky='W', padx = 10, pady = 10)

        ##__fillouts out listbox__##
        def fillout(event):
            productEntry.delete(0, END)
            productEntry.insert(0, listbox.get(ANCHOR))

        ##__Creates canvas on screen__##
        canvas = Canvas(root, width = 875, height = 315)
        canvas.grid(row=0, column=0, columnspan=8, sticky='NWSE', padx = 50, pady = 10)

        ##__narrows down the listbox from entry search__##
        def scankey(event): # grabs the entrybox
            val = event.widget.get()
    
            if val == "":
                data = productFile
            else: # puts characters in list and compares to listbox
                data = []
                for item in productFile:
                    if val.upper() in item.upper():
                        data.append(item)
            update(data)

        ##__Displaying image in canvas__##
        def lickboxSelect(event):
            img = Image.open(path + "\\" + productEntry.get()) # open image from file
            img2 = img.resize((400, 300), Image.ANTIALIAS) # resizes the image to fit the canvas
            img3 = ImageTk.PhotoImage(img2) # adds the images to the tkinter system
            canvas.image = img3 # adds the image to canvas
            canvas.create_image(400, 150, anchor=CENTER, image=img3) # displays the images on canvas
            
        ##__Delete Function__##
        def delete():
            deleteEntry = productEntry.get() # grabbed item from entry box
            str(deleteEntry) # converted into str
            listbox.delete(ANCHOR) # deleted the item u selected
            os.remove(path + "\\" + deleteEntry) # removed it from the path location
            refresh(warehouseGO) # triggered the refresh function

        ##__Delete button__##
        deleteButton =  Button(root, text="Delete", command=delete) # creates the button
        deleteButton.grid(row = 8, column = 0, sticky = 'W', padx = 220) # position

        #__listbox bind__#
        listbox.bind("<<ListboxSelect>>", fillout)
        listbox.bind('<Double-Button-1>', lickboxSelect)
        #__Entry search bind__#
        productEntry.bind("<KeyRelease>", scankey)

        update(productFile)  # Add the items in to the listbox
warehouseGO = WarehouseGO()
root.mainloop()