from datetime import date
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector
# Designing window for registration
 
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def purchase(itemID, color, factory, productionYear, powerSupply, productID, customerID):
    print(itemID, productID, color, factory, productionYear, powerSupply, customerID)

    today = date.today()
    d1 = today.strftime("%y/%m/%d")

    sql3 = "INSERT INTO Item (itemID, productID, purchaseStatus, colour, powerSupply, factory, productionYear) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val3 = [itemID, productID, "SOLD", color, powerSupply, factory, productionYear]
    mycursor.execute(sql3, val3)
    mydb.commit()
    
    #populate buys
    sql2 = "INSERT INTO Buys (itemID, purchasedByCustID, purchaseDate) VALUES (%s, %s, %s) "
    val2 = [itemID, customerID, d1]
    mycursor.execute(sql2, val2)
    mydb.commit()