from tkinter.constants import W
from tkinter import messagebox
from tkinter import *
import mysql.connector
    
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()    
    
def getCustItems(customerID):
    sql = "SELECT itemID from Buys WHERE purchasedByCustID = %s"
    val = [customerID]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    output = []
    
    for i in myresult:

        sql1 = "SELECT productID, colour, powerSupply, factory, productionYear FROM Item WHERE itemID = %s"
        val1 = [i[0]]
        mycursor.execute(sql1,val1)
        #this will be one tuple of (productID, color, powersupply, factory, productionYear)
        myresult1 = mycursor.fetchall()

        sql2 = "SELECT category, model FROM Product WHERE productID = %s"
        val2 = [myresult1[0][0]]
        mycursor.execute(sql2, val2)
        myresult2 = mycursor.fetchall()

        #1 TUPLE of (category, model, productID, color, powersSupply, factory, productionYear)
        result = myresult[0] + myresult2[0] + myresult1[0][1:]
        output.append(result)

    if len(output) == 0:
            messagebox.showinfo(message="No items!")
    
    return output