from datetime import date
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector
# Designing window for approval
 
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def approves(requestID, administratorID):

    sql = "UPDATE ServiceRequest SET requestStatus = %s"
    val = ["Approved"]
    mycursor.execute(sql,val)
    mydb.commit()

    sql1 = "UPDATE Services SET serviceStatus = %s"
    val1 = ["In progress"]
    mycursor.execute(sql1,val1)
    mydb.commit()

    today = date.today()
    d1 = today.strftime("%y/%m/%d")

    sql2 = "INSERT INTO Approves (approvedByAdminID, requestID, approvalDate) VALUES (%s, %d, %s)"
    val2 = [administratorID, requestID, d1]
    mycursor.execute(sql2,val2)
    mydb.commit()




    sql = "SELECT requestID from ServiceRequest"
    mycursor.execute(sql)
    allItems = mycursor.fetchall()
    output = []
    approvedItems = []
    
    for i in allItems:
        sql1 = "SELECT requestID FROM Approves WHERE requestID = %s"
        val1 = [i[0]]
        mycursor.execute(sql1,val1)
        result = mycursor.fetchall()

        if len(result) > 0:
            approvedItems.append(result[0])

    for i in allItems:
        print(i)
        if approvedItems != []:
            if i[0] in approvedItems[0]:
                itemInfo = [i[0], "Approved"]
        else:
            itemInfo = [i[0], "Not Approved"]
        output.append(itemInfo)

    if len(output) == 0:
            messagebox.showinfo(message="Nothing Sold!")
    
    return output