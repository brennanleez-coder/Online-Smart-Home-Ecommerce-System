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

def initialiseItemStatus():
    
    mycursor.execute("CREATE TABLE itemStatus (pID VARCHAR(4) NOT NULL, soldItems INT , unsoldItems INT)")
    mydb.commit()
    
    sql1 = "INSERT INTO itemStatus (pID, soldItems, unsoldItems) VALUES (%s, %s, %s)"
    val1 = [("001", "90", "9"), ("002", "136", "163"), ("003", "29", "74"), ("004", "31","54"), ("005", "46", "99"), ("006", "50", "95"), ("007", "43", "82")]
    mycursor.executemany(sql1, val1)
    mydb.commit() 

    sql2 = "SELECT * FROM itemStatus"
    mycursor.execute(sql2)
    myresult2 = mycursor.fetchall()

    product1 = myresult2[0][0] + "Unsold Items:" + myresult2[0][1] + "Sold items: " + myresult2[0][0] 

    messagebox.showinfo(message="Initialised!")
    """
    sql1 = "INSERT INTO Customer (customerID, fName, lName, gender, emailAddress, address, phoneNumber, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val1 = [("C1", "brennan","lee","male","123@gmail.com","TH","12341234","123"), ("C2", "ryan","tan","male","123@gmail.com","SH","12341234","123"), ("C3", "xinyen","tan","female","123@gmail.com","SH","12341234","123")]
    mycursor.executemany(sql1,val1)x
    mydb.commit()


    sql2 = "INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (%s, %s %s, %s, %s, %s)"
    val2 = ("1", "10", "50", "20", "Light1", "Lights")
    mycursor.execute(sql2,val2)
    mydb.commit()
"""

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

    initialisation = Button(admin,text="INITIALISATION",height="2",width="30",command=initialiseItemStatus)
    initialisation.place(relx=0.2,rely=0.75)


    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    admin.mainloop()
    


#adminview()








