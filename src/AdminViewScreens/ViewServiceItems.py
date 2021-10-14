from tkinter import *
import os
import mysql.connector
from datetime import *
#from CustomerAndAdminFunctions.getSvcItems import getServiceItems
from tkinter import messagebox


mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def viewServiceItemsScreen():

    output = getServiceItems()

    if len(output) != 0:  
        global svcItems_screen
        svcItems_screen = Tk()
        svcItems_screen.geometry("400x500") 
        svcItems_screen.resizable(False, False)

        svcItems_screen.title("Service Items")
        Label(svcItems_screen,text="SERVICE ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
        # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.

        scrollbar = Scrollbar(svcItems_screen)
        scrollbar.pack( side = RIGHT, fill = Y )
        mylist = Listbox(svcItems_screen, yscrollcommand = scrollbar.set, selectmode="multiple")

        # output is a list of tuples
        for items in output:
            mylist.insert(END, "RequestID: " + str(items[0]) + ", itemID: " + items[2] + ", status: "+ items[1])
        
        mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
        scrollbar.config( command = mylist.yview )

        
        Button(svcItems_screen, text="ApproveRequest", height="2", width="30", command = lambda: approves(mylist.curselection(),output)).pack()
        Button(svcItems_screen, text="Complete Servicing", height="2", width="30", command = lambda: completeServicing(mylist.curselection(),output)).pack()
        # soldItems_screen.mainloop()

# viewSoldItemsScreen()


def approves(itemIndexes, itemInfo):
    print(itemIndexes)
    print(itemInfo)
    for i in itemIndexes:
        requestID = itemInfo[i][0]
        print(requestID)
        requestStatus = itemInfo[i][1]

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

        sql2 = "INSERT INTO Approves (approvedByAdminID, requestID, approvalDate) VALUES (%s, %s, %s)"
        val2 = ["A1", requestID, d1]
        mycursor.execute(sql2,val2)
        mydb.commit()

        messagebox.showinfo(title="Approved Successful",
                        message="Item's service request successfully approved!")

def completeServicing(itemIndexes, itemInfo):

    for i in itemIndexes:
        requestID = itemInfo[i][0]
        itemID = itemInfo[i][1]

        sql = "UPDATE ServiceRequest SET requestStatus = %s WHERE requestID = %s"
        val = ["Completed", requestID]
        mycursor.execute(sql,val)
        mydb.commit()

        sql1 = "UPDATE Services SET serviceStatus = %s"
        val1 = ["Completed"]
        mycursor.execute(sql1,val1)
        mydb.commit()

        messagebox.showinfo(title="Servicing Successful",
                        message="Items successfully serviced.")



def getServiceItems():
    
    output = []
    ### RETURNS ALL THOSE WHO SUBMITTED SERVICE REQUEST THAT IS NOT APPROVED OR CANCELLED
    # myresult (requestID, itemID, customerId, requestStatus, requestDate)
    sql = "SELECT requestID, requestStatus, itemID FROM ServiceRequest WHERE requestStatus = %s OR requestStatus = %s OR requestStatus = %s"
    val = ["Submitted", "In Progress", "Approved"]
    mycursor.execute(sql,val)
    result = mycursor.fetchall()

    if len(result) > 0:
        for i in result:
            output.append(i)

    if len(output) == 0:
            messagebox.showinfo(message="Nothing in Service!")

    return output