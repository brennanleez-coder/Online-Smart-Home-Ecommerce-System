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
    print(output)
    if len(output) != 0:    
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

        # output is a list of tuples


        #########TEST############ REMOVE WHEN DONE
        itemList = []
        ############################################
        for items in output:
            mylist.insert(END, items[0] + " " + items[1] + " " + items[2] + " " + items[3] + " " + items[4] + " " + "FACTORY" + " " + items[6])
            itemInfo = (items[0], items[1], items[2], items[3], items[4], items[5], items[6])


            ###########TEST########### REMOVE WHEN DONE
            itemList.append(itemInfo)
            ############################################

        
        mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
        scrollbar.config( command = mylist.yview )




        ################## HOW COME SELECT ONE ITEM BUT DOES NOT RETURN THE WHOLE ARRAY OF ITEM DETAILS ##################################################
        Button(viewProducts, width=10, height=1, text="View Item", command= lambda: viewSingleItem(customerID, itemList, mylist.curselection())).pack(pady=10)



def viewSingleItem(customerID, itemList, itemCursorSelection):
    global viewSingle
    viewSingle=Toplevel()
    #viewSingle.title("ITEM " + str(item[0]+1))
    viewSingle.title("ITEM " + str(itemCursorSelection[0] + 1))
    viewSingle.geometry("350x240")
    viewSingle.resizable(False, False)

    """ img = PhotoImage(file="img/1.png")
    label = Label(viewSingle,image=img)
    label.place(x=0, y=0) """

    singledOutItem = itemList[itemCursorSelection[0]]
    Label(viewSingle,text="ITEM " + str(itemCursorSelection[0]+1),fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack()

    Button(viewSingle, width=20, height=2, text="Request Service", command= lambda: requestService(customerID, singledOutItem)).pack(pady=5)
    Button(viewSingle, width=20, height=2, text="Pay for Service", command= lambda: servicePayment(customerID, item)).pack()
    Button(viewSingle, width=20, height=2, text="Cancel Request", command= lambda: cancelRequest(customerID, item)).pack(pady=5)

def requestService(customerID, item):
    print(item)
   
    model = item[1]
    category = item[2]

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


    sql1 = "SELECT purchaseDate from Buys WHERE itemID = %s"
    val1 = [item[0]]
    mycursor.execute(sql1,val1)
    myresult3 = mycursor.fetchall()
    print(myresult3)

    
    
    warrantyInWeeks = 4 * warranty
    warrantyEndDate = myresult3[0][0] + timedelta(weeks=warrantyInWeeks)
    print(warrantyEndDate)
    #request date
    now = date.today()

    print(now)
    
    if now <= warrantyEndDate:
        requestStatus = "Submitted"
    else:
        requestStatus = "Submitted and Waiting for payment"

    """ sql1 = "SELECT purchasedByCustID from Buys WHERE itemID = %s"
    val1 = [item[0]]
    mycursor.execute(sql1,val1)
    myresult1 = mycursor.fetchall()
    """

    now.strftime("%y/%m/%d")
    
    sql2 = "INSERT INTO ServiceRequest (createdByCustID, requestStatus, requestDate) VALUES (%s, %s, %s)"
    val2 = [customerID, requestStatus, now]
    mycursor.execute(sql2,val2)
    mydb.commit()
    


    """ if requestStatus == "Submitted and Waiting for payment": """


    ##################UPDATE SERVICE STATUS AFTER SEVICE FEE IS PAID##################################################### KIV
    #update for the admin


    """  
        sql3 = "UPDATE Item SET serviceStatus = %s"
        val3 = ["Waiting for approval"]
        mycursor.execute(sql2,val2)
        mydb.commmit() """

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

    global customerID
    customerID = customerIDInput;

    img = PhotoImage(file="img/girl.png")
    label = Label(customer,image=img)
    label.place(x=0, y=0)

    Label(customer,text="Hi Customer,",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack(anchor=NE)
    Label(customer,text="What would you like to do?",fg='Gold', bg='Maroon', width="300", height="2", font = "Helvetica 28 bold").pack()

    searchButton = Button(customer,text="Search Items",height="2",width="30",command=lambda: searchScreen(customerID))
    searchButton.place(relx=0.2,rely=0.45)

    viewButton = Button(customer,text="View Purchased Items",height="2",width="30",command=lambda: view_products(customerID))
    viewButton.place(relx=0.2,rely=0.55)

    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    customer.mainloop()
    

#customerview("1")