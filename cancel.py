from datetime import date
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector
# Designing window for cancellation
 
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def cancelled(requestID, cancellationDate, customerID):
    sql = "UPDATE ServiceRequest SET requestStatus = %s"
    val = ["Canceled"]
    mycursor.execute(sql,val)
    mydb.commit()

    sql1 = "UPDATE Services SET serviceStatus = %s"
    val1 = [""]
    mycursor.execute(sql1,val1)
    mydb.commit()

    sql2 = "INSERT INTO cancels (requestID, cancellationDate, cancelledByCustID) VALUES (%d, %s, %s)"
    val2 = [requestID, cancellationDate, customerID]


def systemCancels(requestID, customerID):

    sql = "SELECT RequestDate FROM ServiceRequest WHERE requestID = %d"
    val = [requestID]
    mycursor.execute(sql,val)
    rDate = mycursor.fetchall()

    sql1 = "SELECT settlementDate FROM ServiceFee WHERE requestID = %d"
    val1 = [requestID]
    mycursor.execute(sql1,val1)
    sDate = mycursor.fetchall()

    today = date.today()
    now = today.strftime("%d/%m/%Y")

    if sDate == "":
        if now > rDate + timedelta(days = 10):
            cancelled(requestID, now, customerID)

def custCancels(requestID, customerID):
    sql = "SELECT RequestDate FROM ServiceRequest WHERE requestID = %d"
    val = [requestID]
    mycursor.execute(sql,val)
    rDate = mycursor.fetchall()

    sql1 = "SELECT settlementDate FROM ServiceFee WHERE requestID = %d"
    val1 = [requestID]
    mycursor.execute(sql1,val1)
    sDate = mycursor.fetchall()

    sql2 = "SELECT requestStatus FROM ServiceRequest WHERE requestID = %d"
    val2 = [requestID]
    mycursor.execute(sql2,val2)
    rStatus = mycursor.fetchall()

    today = date.today()
    now = today.strftime("%d/%m/%Y")

    if rStatus == "Submitted and Waiting for payment" or rStatus == "Submitted" :
        ## add in button to press cancel
        cancelled(requestID, now, customerID)



            



