from tkinter import *
import os
import mysql.connector

def viewUnpaidCustScreen():
    global unpaidCust_screen
    unpaidCust_screen = Tk()
    unpaidCust_screen.geometry("300x350")
    unpaidCust_screen.resizable(False, False)

    unpaidCust_screen.title("Unpaid Customers")
    Label(unpaidCust_screen,text="CUSTOMERS WITH UNPAID ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.


    ########## myresult (itemID, custID, requestDate) returns all the customer who has items that need servicing
    sql = "SELECT itemID, createdByCustID , requestDate FROM ServiceRequest WHERE requestStatus = %s"
    val = ["Submitted and Waiting for payment"]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()

    

    Button(unpaidCust_screen, text="Hi", height="2", width="30", command ={}).pack()
    

    # soldItems_screen.mainloop()

# viewSoldItemsScreen()


