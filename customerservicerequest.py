from datetime import datetime



def makeServiceRequest(itemID):
    sql = "SELECT itemID, purchaseDate FROM Buys WHERE itemID = %s"
    val = [itemID]
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    retrievedItemID = myresult[0]
    retrievedPurchaseDate = myresult[1] // #dd/mm/yyyy
    date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')



