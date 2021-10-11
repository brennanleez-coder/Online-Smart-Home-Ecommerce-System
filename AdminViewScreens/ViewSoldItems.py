from tkinter import *
import os
import mysql.connector

def viewSoldItemsScreen():
    global soldItems_screen
    soldItems_screen = Tk()
    soldItems_screen.geometry("300x350")
    soldItems_screen.resizable(False, False)

    soldItems_screen.title("Sold Items")
    Label(soldItems_screen,text="SOLD ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.

    

    Button(soldItems_screen, text="Hi", height="2", width="30", command ={}).pack()
    # soldItems_screen.mainloop()

# viewSoldItemsScreen()