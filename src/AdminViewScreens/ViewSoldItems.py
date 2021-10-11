from tkinter import *
import os
import mysql.connector
from CustomerAndAdminFunctions.getSoldItems import getSoldItems

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def viewSoldItemsScreen():

    output = getSoldItems()

    if len(output) != 0:  
        global soldItems_screen
        soldItems_screen = Tk()
        soldItems_screen.geometry("300x350")
        soldItems_screen.resizable(False, False)

        soldItems_screen.title("Sold Items")
        Label(soldItems_screen,text="SOLD ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
        # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.

        scrollbar = Scrollbar(soldItems_screen)
        scrollbar.pack( side = RIGHT, fill = Y )
        mylist = Listbox(soldItems_screen, yscrollcommand = scrollbar.set, selectmode="single")

        # output is a list of tuples
        for items in output:
            mylist.insert(END, "ItemID: " + str(items[0]) + ", " + items[1])
        
        mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
        scrollbar.config( command = mylist.yview )