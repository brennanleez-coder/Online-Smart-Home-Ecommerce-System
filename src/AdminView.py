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

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def initialise():
    

    
    sql1 = "INSERT INTO Customer (customerID, fName, lName, gender, emailAddress, address, phoneNumber, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val1 = [("C1", "brennan","lee","male","123@gmail.com","TH","12341234","123"), ("C2", "ryan","tan","male","123@gmail.com","SH","12341234","123"), ("C3", "xinyen","tan","female","123@gmail.com","SH","12341234","123")]
    mycursor.executemany(sql1,va1)
    mydb.commit()


    sql2 = "INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (%s, %s %s, %s, %s, %s)"
    val2 = [(1, 10, 50, 20, "Light1", "Lights"),
        (2, 8, 60, 22, "Light2", "Lights"),
        (3, 8, 70, 30, "Light3", "Lights"),
        (4, 10, 100, 30, "SmartHome1", "Lights"),
        (5, 10, 120, 50, "Safe1", "Locks"),
        (6, 10, 125, 50, "Safe2", "Locks"),
        (7, 12, 200, 100, "SmartHome1", "Locks"),
        ]
    mycursor.executemany(sql2,val2)

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

    initialisation = Button(admin,text="INITIALISATION",height="2",width="30",command=initialise())
    initialisation.place(relx=0.2,rely=0.65)


    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    admin.mainloop()
    


#adminview()








