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
    d1 = today.strftime("%d/%m/%Y")

    sql2 = "INSERT INTO Approves (approvedByAdminID, requestID, approvalDate) VALUES (%s, %d, %s)"
    val2 = [administratorID, requestID, d1]
    mycursor.execute(sql2,val2)
    mydb.commit()