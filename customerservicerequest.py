from datetime import date
from tkinter.constants import W
from datetime import timedelta


def customerMakesServiceRequest(itemID, itemInfo):
    sql = "SELECT itemID, purchaseDate FROM Buys WHERE itemID = %s"
    val = [itemID]
    mycursor.execute(sql,val)
    mydb.commit()
    myresult = mycursor.fetchall()
    retrievedItemID = myresult[0]
    retrievedPurchaseDate = myresult[1] // #dd/mm/yyyy

    model = itemInfo['model']
    category = itemInfo['Category']

    if model == "Light1":
        warranty = 10
    elif model == "Light2":
        warranty = 6
    elif model == "Safe1" or "Safe2" or "Safe3" :
        warranty = 10
    else:
        if model == "SmartHome1":
            if category == "Lights":
                warranty = 8
            else:
                warranty = 12
    
    warrantyInWeeks = 4 * warranty
    warrantyEndDate = retrievedPurchaseDate + timedelta(weeks=warrantyInWeeks)

    #request date
    now = date.today().strftime("%d/%m/%Y") 

    if now <= warrantyEndDate:
        requestStatus = "Submitted"
    else:
        requestStatus = "Submitted and Waiting for payment"

    sql1 = "SELECT purchasedByCustID from Buys WHERE itemID = %s"
    val1 = [itemID]
    mycursor.execute(sql1,val1)
    myresult1 = mycursor.fetchall()

    

    
    sql2 = "INSERT INTO ServiceRequest (createdByCustID, requestStatus, requestDate) VALUES (%s, %s, %s)"
    val2 = [myresult1, requestStatus, now]
    mycursor.execute(sql2,val2)
    mydb.commmit()
    


    if requestStatus == "Submitted and Waiting for payment":


    ##################UPDATE SERVICE STATUS AFTER SEVICE FEE IS PAID##################################################### KIV
    #update for the admin


    
    sql3 = "UPDATE Item SET serviceStatus = %s"
    val3 = ["Waiting for approval"]
    mycursor.execute(sql2,val2)
    mydb.commmit()




    



