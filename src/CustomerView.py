from tkinter import *
import mysql.connector
from typing import Type
from pymongo.message import query
from InitialiseMongoDB import initialiseMongoDB
from tkinter import messagebox
from tkinter.constants import W
from SearchFunctions import searchScreen
from CustomerAndAdminFunctions.getCustItems import getCustItems
from datetime import *

mydb = mysql.connector.connect(user='root', password='password',
                               host='localhost',
                               database='OSHES')

mycursor = mydb.cursor()


def view_products(customerID):

    output = getCustItems(customerID)
    if len(output) != 0:
        global viewProducts
        global options
        global clicked
        viewProducts = Toplevel()
        viewProducts.title("Products Purchased")
        viewProducts.geometry("500x600")
        viewProducts.resizable(False, False)

        Label(viewProducts, text="CUSTOMER " + customerID + " ITEMS", fg='Gold',
              bg='Maroon', width="300", height="3", font="Helvetica 20 bold").pack()

        scrollbar = Scrollbar(viewProducts)
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(
            viewProducts, yscrollcommand=scrollbar.set, selectmode="single")

        # output is a list of tuples
        for items in output:
            mylist.insert(END, items[0] + " " + items[1] + " " + items[2] +
                          " " + items[3] + " " + items[4] + " " + items[5] + " " + items[6])
            itemInfo = (items[0], items[1], items[2],
                        items[3], items[4], items[5], items[6])

        mylist.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        scrollbar.config(command=mylist.yview)

        ################## HOW COME SELECT ONE ITEM BUT DOES NOT RETURN THE WHOLE ARRAY OF ITEM DETAILS ##################################################
        Button(viewProducts, width=10, height=1, text="View Item", command=lambda: viewSingleItem(
            customerID, output, mylist.curselection())).pack(pady=10)


def viewSingleItem(customerID, itemList, itemCursorSelection):
    # TUPLE OF SINGLE ITEM SELECTED FROM LIST
    itemSelected = itemList[itemCursorSelection[0]]

    global viewSingle
    viewSingle = Toplevel()
    viewSingle.title("ITEM " + itemSelected[0])
    viewSingle.geometry("370x280")
    viewSingle.resizable(False, False)


    mydb.commit()
    # GET REQUEST ID
    sql1 = "SELECT max(requestID) FROM ServiceRequest WHERE itemID = %s"
    val1 = [itemSelected[0]]
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()

    sql1 = "SELECT requestStatus FROM ServiceRequest WHERE requestID = %s"
    val1 = [myresult[0][0]]
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()


    print(myresult)

    
    if myresult == []:
        status = "No request"
    else:
        index = len(myresult) - 1
        status = myresult[index][0]
        if status == 'Canceled':
            status = "No request"
        
    print("status")
    print(status)

    # CHECK IF STATUS IS SUBMITTED AND WAITING FOR PAYMENT, IF YES THEN CHECK IF 10 DAYS, IF YES UPDATE TO CANCEL.
    if status == "Submitted and Waiting for payment":
        
        status = checkStatus(status, itemSelected[0])

    Label(viewSingle, text="ITEM " + itemSelected[0], fg='Gold',
          bg='Maroon', width="300", height="3", font="Helvetica 20 bold").pack()

    Label(viewSingle, text="Request Status: " + status, fg='Grey',
          width="300", height="2", font="Helvetica 16").pack()

    if status == "No request" or status == "Canceled" or status == "Completed":
        Button(viewSingle, width=20, height=2, text="Request Service",
           command=lambda: [requestService(customerID, itemSelected), viewSingle.destroy()]).pack(pady=5)

    if status == "Submitted and Waiting for payment":
        Button(viewSingle, width=20, height=2, text="Pay for Service",
               command=lambda: [servicePayment(customerID, itemSelected), viewSingle.destroy()]).pack()

    if status == "In Progress" or status == "Submitted" or status == "Submitted and Waiting for payment":
        Button(viewSingle, width=20, height=2, text="Cancel Request",
               command=lambda: [cancelRequest(itemSelected), viewSingle.destroy()]).pack(pady=5)

###NEED TO UPDATE STATUS TO CANCELED IF SERVICE FEE NOT PAID IN 10 DAYS######


def checkStatus(status, itemID):
    
    sql1 = "SELECT max(requestID) FROM ServiceRequest WHERE itemID = %s"
    val1 = [itemID]
    mycursor.execute(sql1, val1)
    requestID = mycursor.fetchall()
    print("checking requestID:")
    print(requestID)

    sql2 = "SELECT creationDate from ServiceFee WHERE requestID = %s"
    val2 = [requestID[0][0]]
    mycursor.execute(sql2, val2)
    creationDate = mycursor.fetchall()

    today = date.today()
    d1 = today.strftime("%y/%m/%d")
    print(creationDate)
    print("today:")
    print(today)
    endDate = creationDate[0][0] + timedelta(days=10)

    if endDate < today:
        print('here')
        sql4 = "UPDATE ServiceRequest SET requestStatus = %s"
        val4 = ["Canceled"]
        mycursor.execute(sql4, val4)
        mydb.commit()
        return "Canceled"
    else:
        return status


def requestService(customerID, item):
    itemID = item[0]
    model = item[1]
    category = item[2]

    warranty = checkWarranty(model)



    sql1 = "SELECT purchaseDate from Buys WHERE itemID = %s"
    val1 = [itemID]
    mycursor.execute(sql1, val1)
    myresult3 = mycursor.fetchall()

    warrantyInWeeks = 4 * warranty
    warrantyEndDate = myresult3[0][0] + timedelta(weeks=warrantyInWeeks)
    # request date
    now = date.today()

    if now <= warrantyEndDate:
        requestStatus = "Submitted"

    else:
        requestStatus = "Submitted and Waiting for payment"

    now.strftime("%y/%m/%d")

    sql2 = "INSERT INTO ServiceRequest (itemID, createdByCustID, requestStatus, requestDate) VALUES (%s, %s, %s, %s)"
    val2 = [itemID, customerID, requestStatus, now]
    mycursor.execute(sql2, val2)
    mydb.commit()

    sql3 = "INSERT INTO Services (serviceStatus, servicedByAdminID, itemID) VALUES (%s, %s, %s)"
    val3 = ["Waiting for approval", "A1", itemID]
    mycursor.execute(sql3, val3)


# CREATION OF SERVICE FEE HERE.
    cost = checkCost(model)


    # GET REQUEST STATUS TO COMPUTE THE SERVICE FEES
    sql3 = "SELECT requestStatus FROM ServiceRequest WHERE itemID = %s"
    val3 = [itemID]
    mycursor.execute(sql3, val3)
    myresult = mycursor.fetchall()
    requestStatus = myresult[0][0]

    if requestStatus == "Submitted and Waiting for payment":
        serviceFEE = int(40 + 0.2*cost)
    else:
        serviceFEE = 0

    sql4 = "SELECT max(requestID) FROM ServiceRequest WHERE itemID = %s"
    val4 = [itemID]
    mycursor.execute(sql4, val4)
    myresult1 = mycursor.fetchall()
    requestID = myresult1[0][0]
    print("requestID")
    print(requestID)


    sql4 = "SELECT RequestDate FROM ServiceRequest WHERE requestID = %s"
    val4 = [requestID]
    mycursor.execute(sql4, val4)
    myresult2 = mycursor.fetchall()
    requestDate = myresult2[0][0]
    print("requestDate: ")
    print(requestDate)

    sql5 = "INSERT INTO ServiceFee (requestID, serviceFeeAmount, creationDate) VALUES (%s, %s, %s)"
    val5 = [requestID, serviceFEE, requestDate]
    mycursor.execute(sql5, val5)
    mydb.commit()

    messagebox.showinfo(title="Service Request Submitted",
                        message="Successful!")


def servicePayment(customerID, item):
    print("paying for service: ")
    itemID = item[0]

    sql3 = "SELECT requestStatus FROM ServiceRequest WHERE itemID = %s"
    val3 = [itemID]
    mycursor.execute(sql3, val3)
    myresult = mycursor.fetchall()
    # SINGLE STRING TUPLE

    # NO REQUEST AT ALL.
    if myresult == []:
        messagebox.showinfo(message="No request currently!")
    else:
        # NO SERVICE FEE AT ALL.

        # GET REQUEST ID
        sql1 = "SELECT max(requestID) FROM ServiceRequest WHERE itemID = %s"
        val1 = [itemID]
        mycursor.execute(sql1, val1)
        myresult = mycursor.fetchall()
        requestID = myresult[0][0]

        # QUERY FOR COST OF FEE
        sql2 = "SELECT serviceFeeAmount FROM ServiceFee WHERE requestID = %s"
        val2 = [requestID]
        mycursor.execute(sql2, val2)
        myresult = mycursor.fetchall()
        serviceFEE = myresult[0][0]
        print(serviceFEE)

        if serviceFEE == 0:

            messagebox.showinfo(title="Good news,",
                                message="No payment required!")
        else:
            paymentDate = date.today().strftime("%y/%m/%d")

            sql3 = "INSERT INTO Payment (paidByCustID, paymentDate, paymentAmount) VALUES (%s, %s, %s)"
            val3 = [customerID, paymentDate, serviceFEE]
            mycursor.execute(sql3, val3)
            mydb.commit()

            sql4 = "UPDATE ServiceRequest SET requestStatus = %s"
            val4 = ["In Progress"]
            mycursor.execute(sql4, val4)
            mydb.commit()

            sql5 = "SELECT paymentID FROM Payment WHERE paymentID=(SELECT max(paymentID) FROM Payment)"
            mycursor.execute(sql5)
            myresult1 = mycursor.fetchall()
            paymentID = myresult1[0][0]

            # UPDATE SERVICEFEE PAYMENTID AND SETTLEMENT DATE ROW.
            sql6 = "UPDATE ServiceFee SET settlementDate = %s, settledByPaymentID = %s"
            val6 = [paymentDate, paymentID]
            mycursor.execute(sql6, val6)
            mydb.commit()

            messagebox.showinfo(title="Service Payment Submitted",
                                message="Successful!")


        #################UPDATE ITEM TABLE IF NEED###########################


def cancelRequest(item):
    print("Cancel Request:")
    itemID = item[0]

    # GET REQUEST ID
    sql1 = "SELECT max(requestID) FROM ServiceRequest WHERE itemID = %s"
    val1 = [itemID]
    mycursor.execute(sql1, val1)
    myresult = mycursor.fetchall()


    if myresult == []:
        print("NOTHING")

        messagebox.showinfo(title="Service Request Cancelled",
                            message="No request to cancel!")

    else:


        requestID = myresult[0][0]
        print(requestID)

        # update REQUESTstatus FROM REQUEST TABLE
        sql3 = "UPDATE ServiceRequest SET requestStatus = %s WHERE requestID = %s"
        val3 = ["Canceled", requestID]
        mycursor.execute(sql3, val3)
        mydb.commit()

        # DELETE from services table because request is cancelled
        sql4 = "DELETE FROM Services WHERE itemID = %s"
        val4 = [itemID]
        mycursor.execute(sql4, val4)
        mydb.commit()

        
        sql5 = "DELETE FROM ServiceFee WHERE requestID = %s"
        val5 = [requestID]
        mycursor.execute(sql5, val5)
        print(mycursor)
        mydb.commit()

        messagebox.showinfo(title="Service Request Cancelled",
                            message="Successful!")


def checkWarranty(model):
    if model == "Light1":
        warranty = 10
    elif model == "Light2":
        warranty = 6
    elif model == "Safe1" or "Safe2" or "Safe3":
        warranty = 10
    else:
        if model == "SmartHome1":
            if category == "Lights":
                warranty = 8
            else:
                warranty = 12
    return warranty

def checkCost(model):
    if model == "Light1":
        cost = 20
    elif model == "Light2":
        cost = 22
    elif model == "Safe1":  
        cost = 30
    elif model == "Safe2" or "Safe3":
        cost = 50
    else:
        if model == "SmartHome1":
            if category == "Lights":
                cost = 30
            else:
                cost = 100
    return cost


# ------------------------------------------ MAIN ---------------------------------------------------------------------------------------------

def customerview(customerIDInput):
    global customer
    customer = Tk()
    customer.title("Customer View")
    customer.geometry("500x600")
    customer.resizable(False, False)

    global customerID
    customerID = customerIDInput

    img = PhotoImage(file="img/girl.png")
    label = Label(customer, image=img)
    label.place(x=0, y=0)

    Label(customer, text="Hi " + customerID + ",", fg='Gold', bg='Maroon',
          width="300", height="2", font="Helvetica 28 bold").pack(anchor=NE)
    Label(customer, text="What would you like to do?", fg='Gold',
          bg='Maroon', width="300", height="2", font="Helvetica 28 bold").pack()

    searchButton = Button(customer, text="Search Items", height="2",
                          width="30", command=lambda: searchScreen(customerID))
    searchButton.place(relx=0.2, rely=0.45)

    viewButton = Button(customer, text="View Purchased Items", height="2",
                        width="30", command=lambda: view_products(customerID))
    viewButton.place(relx=0.2, rely=0.55)

    addInfo = Label(text="© BT2102 GROUP 6.", font="Helvetica 12 italic")
    addInfo.place(relx=0.7, rely=0.9)

    customer.mainloop()
