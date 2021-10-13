from tkinter import *
import os
import mysql.connector
from tkinter import messagebox


mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')
mycursor = mydb.cursor()

def viewUnpaidCustScreen():
    global unpaidCust_screen
    unpaidCust_screen = Tk()
    unpaidCust_screen.geometry("400x400")
    unpaidCust_screen.resizable(False, False)

    unpaidCust_screen.title("Unpaid Customers")
    Label(unpaidCust_screen,text="CUSTOMERS WITH UNPAID ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.


    ########## myresult (itemID, custID, requestDate) returns all the customer who has items that need servicing
    sql = "SELECT itemID, createdByCustID FROM ServiceRequest WHERE requestStatus = %s"
    val = ["Submitted and Waiting for payment"]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    scrollbar = Scrollbar(unpaidCust_screen)
    scrollbar.pack( side = RIGHT, fill = Y )

    for i in myresult:
        Label(unpaidCust_screen, text="Customer " + str(i[0]) + " Unpaid item: " + str(i[1]), font = "Helvetica 16").pack()

    scrollbar.config( command = mylist.yview )