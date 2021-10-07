from datetime import date

def purchase(color, factory, productionYear, powerSupply, customerid, productID):
    sql = "SELECT productID FROM Product where productID= %d"
    val = (productID)
    mydb.commit()
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall() #product

    
    #getItemID
    sql1 = "SELECT itemID FROM Item WHERE color = %s AND factory = %s AND powerSupply = %s productionYear = %s AND purchaseStatus = "SOLD" ORDER BY RAND() LIMIT 1"
    val1 = [%s, %s, %s, %s]
    mydb.commit()
    mycursor.execute(sql1,val1)
    itemIDAvailable = mycursor.fetchall()
   

    

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    #populate buys
    sql2 = "INSERT INTO Buys (itemID, puchasedByCustID, purchaseDate, quantity) VALUES (%s, %d, %s, 1) "
    val2 = [itemIDAvailablem, customerid, d1]
    mycursor.execute(sql1, val1)
    mydb.commit()

    #Update to sold
    sql3 = "UPDATE Item SET purchaseStatus= %s, productID = %s WHERE itemID = %s "
    val3 = ["SOLD", productID, itemIDAvailable]
    mycursor.execute(sql1, val1)
    mydb.commit()

    flash("Item successfully purchased")
    

