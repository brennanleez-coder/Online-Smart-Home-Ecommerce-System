from tkinter import *
import os
import mysql.connector
from typing import Type
from pymongo.message import query
from InitialiseMongoDB import initialiseMongoDB
from pymongo import MongoClient
from tkinter import messagebox
from datetime import date
from tkinter.constants import W
from datetime import timedelta

from SearchFunctions import searchScreen
from AdminViewScreens.ViewSoldItems import viewSoldItemsScreen
from AdminViewScreens.ViewUnpaidCust import viewUnpaidCustScreen
from AdminViewScreens.ViewServiceItems import viewServiceItemsScreen


# ------------------------------------------ MAIN --------------------------------------------------------------------------------------------- 
    
def adminview(adminID):
    global admin
    admin=Tk()
    admin.title("Admin View")
    admin.geometry("500x600")
    admin.resizable(False, False)


    img = PhotoImage(file="img/2.png")
    label = Label(admin,image=img)
    label.place(x=0, y=0)

    Label(admin,text="Hi Admin,",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack(anchor=NE)
    Label(admin,text="What would you like to do?",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack()

    searchButton = Button(admin,text="Search Items",height="2",width="30",command=lambda: searchScreen(adminID))
    searchButton.place(relx=0.2,rely=0.35)

    viewSoldButton = Button(admin,text="View Sold Items",height="2",width="30",command=viewSoldItemsScreen)
    viewSoldButton.place(relx=0.2,rely=0.45)

    viewSvcButton = Button(admin,text="View Service Items",height="2",width="30",command=viewServiceItemsScreen)
    viewSvcButton.place(relx=0.2,rely=0.55)

    unpaidCustButton = Button(admin,text="View Unpaid Customers",height="2",width="30",command=viewUnpaidCustScreen)
    unpaidCustButton.place(relx=0.2,rely=0.65)

    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    admin.mainloop()
    

#adminview()


