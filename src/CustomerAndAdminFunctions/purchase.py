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

def purchase(itemID, model, color, factory, productionYear, powerSupply, customerID):
    print(itemID, model, color, factory, productionYear, powerSupply, customerID)

    """ sql = "SELECT productID FROM Product WHERE model = %s"
    val = [model]
    mycursor.execute(sql,val)
    mydb.commit()
    myresult = mycursor.fetchall()


    today = date.today()
    d1 = today.strftime("%y/%m/%d")
    #populate buys
    sql2 = "INSERT INTO Buys (itemID, purchasedByCustID, purchaseDate, quantity) VALUES (%s, %s, %s, 1) "
    val2 = [itemIDAvailable, customerID, d1]
    mycursor.execute(sql1, val1)
    mydb.commit() """


    """ sql3 = "INSERT INTO Item (itemID, productID, servicedByAdminID, purchaseStatus, serviceStatus, color, powerSupply, factory, productionYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val3 = [itemID, myresult, "", "SOLD", "", color, powerSupply, factory, productionYear]
    mycursor.execute(sql3, val3)
    mydb.commit() """

    #################IMPORTANT######################
    #STATEMENT TO UPDATE MONGODB DATABASE FOR ITEM
    

