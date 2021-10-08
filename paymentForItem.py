from datetime import date
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector

def calculatePayment(items):
    numOfItems = len(items)
    totalPrice = 0
    for i in range(numOfItems):
        sql = "SELECT productID FROM Item WHERE itemID = %s"
        val = [item[i]]
        mycursor.execute(sql,val)
        proID = mycursor.fetchall()

        sql1 = "SELECT price FROM Product WHERE productID = %s"
        val1 = [proID]
        mycursor.execute(sql1,val1)
        price = mycursor.fetchall()

        totalPrice += price

    return totalPrice

def makePaymentForItems(customerID, items):
    today = date.today()
    d1 = today.strftime("%y/%m/%d")

    sql = "INSERT INTO Payment (paidByCustID, paymentDate, paymentAmount) VALUES (%s, %s, %d)"
    val = [customerID, d1, calculatePayment(items)]
    mycursor.execute(sql, val)
    mydb.commit()


        