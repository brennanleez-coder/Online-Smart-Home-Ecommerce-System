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

from SearchFunctions import searchScreen
from AdminViewScreens.ViewSoldItems import viewSoldItemsScreen
from AdminViewScreens.ViewUnpaidCust import viewUnpaidCustScreen
from AdminViewScreens.ViewServiceitems import viewServiceItemsScreen

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


""" 
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
    view=Toplevel()
    view.title("Products Purchased")
    view.geometry("300x250")
    if lst_of_products==[]:
     print("No items purchased")
    else:
        for items in lst_of_products:
            Button(view,text=items[0]+' '+items[1],height="2",width="30",command=manageproducts).pack() """
    
   
# ------------------------------------------ MAIN --------------------------------------------------------------------------------------------- 
    
def adminview(adminID):
    global admin
    admin=Tk()
    admin.title("Admin View")
    admin.geometry("500x600")
    admin.resizable(False, False)


    img = PhotoImage(file="img/2.png")
    label = Label(admin,image=img)
    label.place(x=0, y=0)

    Label(admin,text="Hi Admin,",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack(anchor=NE)
    Label(admin,text="What would you like to do?",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack()

    searchButton = Button(admin,text="Search Items",height="2",width="30",command=lambda: searchScreen("Admin"))
    searchButton.place(relx=0.2,rely=0.35)

    viewSoldButton = Button(admin,text="View Sold Items",height="2",width="30",command=viewSoldItemsScreen)
    viewSoldButton.place(relx=0.2,rely=0.45)

    viewSvcButton = Button(admin,text="View Service Items",height="2",width="30",command=viewServiceItemsScreen)
    viewSvcButton.place(relx=0.2,rely=0.55)

    unpaidCustButton = Button(admin,text="View Unpaid Customers",height="2",width="30",command=viewUnpaidCustScreen)
    unpaidCustButton.place(relx=0.2,rely=0.65)

    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    admin.mainloop()
    

#adminview()


