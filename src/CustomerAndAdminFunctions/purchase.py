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

def purchase(itemID, category, model, colour, factory, productionYear, powerSupply, customerID):
    

    if category == "Lights":
        if model == "Light1":
            productID=1
        elif model == "Light2":
            productID=2
        elif model == "SmartHome1":
            productID=3
    else:
        if model == "SmartHome1":
                productID=7
        elif model == "Safe1":
            productID=4
        elif model == "Safe2":
            productID=5
        elif model == "Safe3":
            productID=6

    

    today = date.today()
    d1 = today.strftime("%y/%m/%d")



    sql3 = "INSERT INTO Item (itemID, productID, purchaseStatus, colour, powerSupply, factory, productionYear) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val3 = [itemID, productID, "SOLD", colour, powerSupply, factory, productionYear]
    mycursor.execute(sql3, val3)
    mydb.commit() 
    
    #populate buys
    sql2 = "INSERT INTO Buys (itemID, purchasedByCustID, purchaseDate) VALUES (%s, %s, %s) "
    val2 = [itemID, customerID, d1]
    mycursor.execute(sql2, val2)
    mydb.commit()
    print(itemID, model, colour, factory, productionYear, powerSupply, customerID)


  
    

