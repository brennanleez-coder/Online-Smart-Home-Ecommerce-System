from tkinter import *
import os
import mysql.connector

def viewServiceItemsScreen():
    global serviceItems_screen
    serviceItems_screen = Tk()
    serviceItems_screen.geometry("300x350")
    serviceItems_screen.resizable(False, False)

    serviceItems_screen.title("Service Items")
    Label(serviceItems_screen,text="SERVICE ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE IN SERVICE (BOTH APPROVED AND NON). QUERY HERE.

    

    Button(serviceItems_screen, text="Hi", height="2", width="30", command ={}).pack()
    # soldItems_screen.mainloop()

# viewSoldItemsScreen()