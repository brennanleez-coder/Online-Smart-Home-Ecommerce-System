from tkinter import *
import os
import mysql.connector
from datetime import *

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def viewServiceItemsScreen():
    global unpaidCust_screen
    unpaidCust_screen = Tk()
    unpaidCust_screen.geometry("400x500")
    unpaidCust_screen.resizable(False, False)

    unpaidCust_screen.title("Unpaid Customers")
    Label(unpaidCust_screen,text="CUSTOMERS WITH UNPAID ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.




    ### RETURNS ALL THOSE WHO SUBMITTED SERVICE REQUEST THAT IS NOT APPROVED OR CANCELLED
    # myresult (requestID, itemID, customerId, requestStatus, requestDate)
    sql = "SELECT * FROM ServiceRequest WHERE requestStatus = %s OR requestStatus = %s OR requestStatus = %s"
    val = ["Submitted", "In progress", "Approved"]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()




    ############ RYAN PLS MAKE LIST############

    
    Button(unpaidCust_screen, text="ApproveRequest", height="2", width="30", command ={approves(mylist.curselection(),myresult)}).pack()
    Button(unpaidCust_screen, text="Complete Servicing", height="2", width="30", command ={completeServicing(mylist.curselection(),myresult)}).pack()
    Button(unpaidCust_screen, text="Hi", height="2", width="30", command ={}).pack()
    # soldItems_screen.mainloop()

# viewSoldItemsScreen()


def approves(listOfItemsThatWantToBeApproved, serviceRequestTableInfo):

    for i in listOfItemsThatWantToBeApproved:
        requestID = serviceRequestTableInfo[0]
        itemID = serviceRequestTableInfo[1]

        sql = "UPDATE ServiceRequest SET requestStatus = %s WHERE requestID = %s"
        val = ["Approved", requestID]
        mycursor.execute(sql,val)
        mydb.commit()

        sql1 = "UPDATE Services SET serviceStatus = %s"
        val1 = ["In progress"]
        mycursor.execute(sql1,val1)
        mydb.commit()

        today = date.today()
        d1 = today.strftime("%y/%m/%d")

        sql2 = "INSERT INTO Approves (approvedByAdminID, requestID, approvalDate) VALUES (%s, %d, %s)"
        val2 = ["ADMIN", requestID, d1]
        mycursor.execute(sql2,val2)
        mydb.commit()

        messagebox.showinfo(title="Approved Successful",
                        message="Item's service request successfully approved!")

def completeServicing(listOfItemsThatWantToBeApproved, serviceRequestTableInfo):

    for i in listOfItemsThatWantToBeApproved:
        requestID = serviceRequestTableInfo[0]
        itemID = serviceRequestTableInfo[1]

        sql = "UPDATE ServiceRequest SET requestStatus = %s WHERE requestID = %s"
        val = ["Completed", requestID]
        mycursor.execute(sql,val)
        mydb.commit()

        sql1 = "UPDATE Services SET serviceStatus = %s"
        val1 = ["Completed"]
        mycursor.execute(sql1,val1)
        mydb.commit()

        messagebox.showinfo(title="Servicing Successful",
                        message="Items successfully serviced")