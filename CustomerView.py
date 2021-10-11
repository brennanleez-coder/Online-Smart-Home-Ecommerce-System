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

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

customerID = ""

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


def view_products(customerID):
    global viewProducts
    global options
    global clicked
    viewProducts=Toplevel()
    viewProducts.title("Products Purchased")
    viewProducts.geometry("500x600")
    viewProducts.resizable(False, False)
    

    Label(viewProducts,text="CUSTOMER " + customerID + " ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack()

    scrollbar = Scrollbar(viewProducts)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(viewProducts, yscrollcommand = scrollbar.set, selectmode="single")


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
    else:
        # output is a list of tuples
        for items in output:
            mylist.insert(END, items[0] + " " + items[1] + " " + items[2] + " " + items[3] + " " + items[4] + " " + items[5] + " " + items[6])
    

    mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
    scrollbar.config( command = mylist.yview )


    Button(viewProducts, width=10, height=1, text="View Item", command= lambda: viewSingleItem(customerID, mylist.curselection())).pack(pady=5)



def viewSingleItem(customerID, item):
    global viewSingle
    viewSingle=Toplevel(viewProducts)
    viewSingle.title("ITEM " + str(item[0]))
    viewSingle.geometry("350x240")
    viewSingle.resizable(False, False)

    """ img = PhotoImage(file="img/1.png")
    label = Label(viewSingle,image=img)
    label.place(x=0, y=0) """
    
    Label(viewSingle,text="ITEM " + str(item[0]),fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack()


    Button(viewSingle, width=20, height=2, text="Request Service", command= lambda: requestService(customerID, item)).pack(pady=5)
    Button(viewSingle, width=20, height=2, text="Pay for Service", command= lambda: requestService(customerID, item)).pack()
    Button(viewSingle, width=20, height=2, text="Cancel Request", command= lambda: requestService(customerID, item)).pack(pady=5)

def requestService(customerID, item):
# LOGIC HERE
    messagebox.showinfo(title="Service Request Submitted",message="Successful!")


def servicePayment(customerID, item):
# LOGIC HERE
    messagebox.showinfo(title="Service Payment Submitted",message="Successful!")


def cancelRequest(customerID, item):
 # LOGIC HERE
   messagebox.showinfo(title="Service Request Cancelled",message="Successful!")



# ------------------------------------------ MAIN --------------------------------------------------------------------------------------------- 

def customerview(customerIDInput):
    global customer
    customer=Tk()
    customer.title("Customer View")
    customer.geometry("500x600")
    customer.resizable(False, False)

    customerID = customerIDInput;

    img = PhotoImage(file="img/girl.png")
    label = Label(customer,image=img)
    label.place(x=0, y=0)

    Label(customer,text="Hi Customer,",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack(anchor=NE)
    Label(customer,text="What would you like to do?",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack()

    searchButton = Button(customer,text="Search Items",height="2",width="30",command=lambda: searchScreen("Customer"))
    searchButton.place(relx=0.2,rely=0.45)

    viewButton = Button(customer,text="View Purchased Items",height="2",width="30",command=lambda: view_products(customerID))
    viewButton.place(relx=0.2,rely=0.55)

    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    customer.mainloop()
    

customerview("1")
#Advanced search
#Add widgets here


