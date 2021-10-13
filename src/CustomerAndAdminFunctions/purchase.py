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

    sql1 = "SELECT * FROM itemStatus WHERE pID = %s "
    val1 = [productID]
    mycursor.execute(sql1, val1)
    result = mycursor.fetchall()
    soldCount = result[0][1]
    unsoldCount = result[0][2]

    unsoldCount -= 1
    soldCount += 1

    sql4 = "UPDATE itemStatus SET unsoldItems = %s, soldItems = %s WHERE pID = %s"
    val4 = [unsoldCount, soldCount, productID]
    mycursor.execute(sql4,val4)
    mydb.commit()
