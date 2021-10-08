from tkinter import *
import os
import mysql.connector
from typing import Type
from pymongo.message import query
from InitialiseMongoDB import initialiseMongoDB
from pymongo import MongoClient
from tkinter import messagebox
from datetime import date
from tkinter.constants import W
from datetime import timedelta
from SearchFunctions import advancedSearch, advancedSearchScreen, simpleSearch, simpleSearchScreen, simpleSearch, checkout


def customerMakesServiceRequest(itemID, itemInfo):
    sql = "SELECT itemID, purchaseDate FROM Buys WHERE itemID = %s"
    val = [itemID]
    mycursor.execute(sql,val)
    mydb.commit()
    myresult = mycursor.fetchall()
    retrievedItemID = myresult[0]
    retrievedPurchaseDate = myresult[1]  #dd/mm/yyyy

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



def successfulsubmission():
    global success
    success=Toplevel(submit)
    messagebox.showinfo(title="Service Request Submitted",message="Successful!")


    
    
def submitservicerequest():
    global submit
    submit=Toplevel(view)
    Button(submit,text="Confirm Submit",height="2",width="30",command=successfulsubmission).pack()
    

    
    
    #Need update to sql/MongoDB?
    
    
def manageproducts():
    Button(view,text="Submit Service Request",height="2",width="30",command=submitservicerequest).pack()
    Button(view,text="Pay Service Fees",height="2",width="30").pack()
    Button(view,text="Cancel Service Request",height="2",width="30").pack()
            

def view_products():
    global view
    global options
    global clicked
    view=Toplevel(customer)
    view.title("Products Purchased")
    view.geometry("300x250")
    if lst_of_products==[]:
        print("No items purchased")
    else:
        for items in lst_of_products:
            Button(view,text=items[0]+' '+items[1],height="2",width="30",command=manageproducts).pack()
    

# ------------------------------------------ MAIN --------------------------------------------------------------------------------------------- 
def searchScreen():
    global search_screen
    search_screen = Tk()
    search_screen.geometry("300x350")
    search_screen.title("Search")
    Button(search_screen, text="Simple Search", height="2", width="30", command = simpleSearchScreen).pack()
    Button(search_screen, text="Advanced Search", height="2", width="30", command = advancedSearchScreen).pack()

    
def customerview():
    global customer
    print("out")
    customer=Tk()
    customer.title("Customer View")
    customer.geometry("300x250")
    Label(customer,text="What would you like to do?",bg='green',width="300",height="1",font=("Calibri",16)).pack()
    Button(customer,text="Search Products",height="2",width="30",command=searchScreen).pack()
    Button(customer,text="View Products",height="2",width="30",command=view_products).pack()
    customer.mainloop()
    

#Advanced search
#Add widgets here


