from datetime import date
from tkinter import messagebox

def purchase(itemID, model, color, factory, productionYear, powerSupply, customerid):
    
    #getItemID
    #sql1 = "SELECT itemID FROM Item WHERE color = %s AND factory = %s AND powerSupply = %s productionYear = %s AND purchaseStatus = "SOLD" ORDER BY RAND() LIMIT 1"
    #val1 = [color, factory, powerSupply, productionYear]
    #mydb.commit()
    #mycursor.execute(sql1,val1)
    #itemIDAvailable = mycursor.fetchall()
   
    sql = "SELECT productID FROM Product WHERE model = %s"
    val = [model]
    mycursor.execute(sql,val)
    mydb.commit()
    myresult = mycursor.fetchall()


    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    #populate buys
    sql2 = "INSERT INTO Buys (itemID, purchasedByCustID, purchaseDate, quantity) VALUES (%s, %d, %s, 1) "
    val2 = [itemIDAvailable, customerID, d1]
    mycursor.execute(sql1, val1)
    mydb.commit()



    



    sql3 = "INSERT INTO Item (itemID, productID, servicedByAdminID, purchaseStatus, serviceStatus, color, powerSupply, factory, productionYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val3 = [itemID, myresult, "", "SOLD", "", color, powerSupply, factory, productionYear]
    mycursor.execute(sql3, val3)
    mydb.commit()

    #################IMPORTANT######################
    #STATEMENT TO UPDATE MONGODB DATABASE FOR ITEM


    messagebox.showinfo("Hi customer", "Item successfully purchased")
    

