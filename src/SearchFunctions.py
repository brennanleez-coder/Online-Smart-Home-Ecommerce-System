from typing import Type
from InitialiseMongoDB import initialiseMongoDB
from pymongo import MongoClient
from tkinter import messagebox
from tkinter import *
import mysql.connector
from CustomerAndAdminFunctions.purchase import purchase

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

client = MongoClient()
initialiseMongoDB(client)

mongoClient = client["bt2102"]
itemsCol = mongoClient["items"]
productsCol = mongoClient["products"]

allCategories = ["Lights", "Locks"]
allModels = ["Light1", "Light2", "SmartHome1", "Safe1", "Safe2", "Safe3"]

def searchScreen(thisUserID):
    global search_screen
    search_screen = Tk()
    search_screen.geometry("300x280")
    search_screen.resizable(False, False)
    Label(search_screen,text="SEARCH",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    
    global userID
    userID = thisUserID

    search_screen.title("Search")
    Button(search_screen, text="Simple Search", height="2", width="30", command = simpleSearchScreen).pack(pady=5)
    Button(search_screen, text="Advanced Search", height="2", width="30", command = advancedSearchScreen).pack()
    if userID[0] == "A":
        Button(search_screen, text="Item Search", height="2", width="30", command = itemSearchScreen).pack(pady=5)


# ------------------------------------------ SIMPLE SEARCH ------------------------------------------------------------------------------------

def simpleSearchScreen():

    global simpleSearch_screen
    simpleSearch_screen = Toplevel()
    simpleSearch_screen.title("Simple Search")
    simpleSearch_screen.geometry("300x300")
    img = PhotoImage(file="img/cart.png")
    label = Label(simpleSearch_screen,image=img)
    label.place(x=0, y=0)

    Label(simpleSearch_screen, text="SIMPLE SEARCH", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()
    Label(simpleSearch_screen, text="Filter by:").pack()
 
    catModel = StringVar()
    global catModelInput

    Label(simpleSearch_screen, text="Category/Model * (Eg. Lights / Light1)").pack()
    catModelInput = Entry(simpleSearch_screen, textvariable=catModel)
    catModelInput.pack()
    
    Button(simpleSearch_screen, text="Search", width=10, height=1, command = lambda: [simpleSearch(catModel), simpleSearch_screen.destroy()]).pack()
    Button(simpleSearch_screen, width=10, height=1, text="Back", command= simpleSearch_screen.destroy).pack()



def simpleSearch(catModel):

    global simpleResults_screen
    simpleResults_screen = Tk()
    simpleResults_screen.title("Simple Search")
    simpleResults_screen.geometry("500x600")
    simpleResults_screen.resizable(False, False)
    Label(simpleResults_screen, text="SEARCH RESULTS", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()

    catModel = catModel.get()

    query = {"PurchaseStatus": "Unsold"}

    if catModel in allCategories:
        query["Category"] = catModel

    if catModel in allModels:
        query["Model"] = catModel

    totalStockCount = itemsCol.find(query, {"_id": 0}).count()

    groupItems = itemsCol.aggregate([{"$match": query}, {"$group": {"_id": {"Color": "$Color", "PowerSupply": "$PowerSupply", "ProductionYear": "$ProductionYear", "Factory": "$Factory", "Product": "$Product", "Category": "$Category", "Model": "$Model"}, "Stock": {"$sum": 1}}}])

    Label(simpleResults_screen, text=totalStockCount).pack()

    scrollbar = Scrollbar(simpleResults_screen)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(simpleResults_screen, yscrollcommand = scrollbar.set, selectmode="multiple")


    groupItemData = []
    for i in groupItems:
        x = i.get("_id")

        prod = productsCol.find({"Category": str(x.get("Category")), "Model": str(x.get("Model"))})
        for p in prod:
            if (p.get("Model") == x.get("Model")) and (p.get("Category") == x.get("Category")):
                x["ProductID"] = p.get("ProductID")
                x["Warranty"] = p.get("Warranty (months)")
                x["Price"] = p.get("Price ($)")
                x["Cost"] = p.get("Cost ($)")


        mylist.insert(END, str(x.get("Category")) + ", " + str(x.get("Model")) + ", " + str(x.get("Color")) + ", $" + str(x.get("Price")) + ", " + str(x.get("Warranty")) + " Months Warranty, " + str(i.get("Stock")) + " Left")
        groupItemData.append(x)
    
    mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
    scrollbar.config( command = mylist.yview )

    Button(simpleResults_screen, width=10, height=1, text="Checkout", command= lambda: checkout(groupItemData, mylist.curselection())).pack()
    Button(simpleResults_screen, width=10, height=1, text="Close", command= simpleResults_screen.destroy).pack()

    catModelInput.delete(0, END)



# ------------------------------------------ ADVANCED SEARCH ------------------------------------------------------------------------------------ 

def advancedSearchScreen():

    global advancedSearch_screen
    advancedSearch_screen = Toplevel()
    advancedSearch_screen.title("Advanced Search")
    advancedSearch_screen.geometry("500x550")
    Label(advancedSearch_screen, text="ADVANCED SEARCH", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()
    Label(advancedSearch_screen, text="Filter by:").pack()
 
    catModel = StringVar()
    color = StringVar()
    factory = StringVar()
    prodYear = StringVar()
    powerSupply = StringVar()
    global catModelInput, colorInput, factoryInput, prodYearInput, powerSupplyInput

    Label(advancedSearch_screen, text="Category/Model * (Eg. Lights / Light1)").pack()
    catModelInput = Entry(advancedSearch_screen, textvariable=catModel)
    catModelInput.pack()

    Label(advancedSearch_screen, text="Color (White / Blue / Yellow / Green / Black)").pack()
    colorInput = Entry(advancedSearch_screen, textvariable=color)
    colorInput.pack()

    Label(advancedSearch_screen, text="Factory (Malaysia / China / Philippines)").pack()
    factoryInput = Entry(advancedSearch_screen, textvariable=factory)
    factoryInput.pack()

    Label(advancedSearch_screen, text="Production Year (YYYY) ").pack()
    prodYearInput = Entry(advancedSearch_screen, textvariable=prodYear)
    prodYearInput.pack()

    Label(advancedSearch_screen, text="Power Supply (USB / Battery)").pack()
    powerSupplyInput = Entry(advancedSearch_screen, textvariable=powerSupply)
    powerSupplyInput.pack()
    
    Button(advancedSearch_screen, text="Search", width=10, height=1, command = lambda: [advancedSearch(catModel, color, factory, prodYear, powerSupply), advancedSearch_screen.destroy()]).pack()
    Button(advancedSearch_screen, width=10, height=1, text="Back", command= advancedSearch_screen.destroy).pack(pady=20)


# RETURNS ALL SEARCH RESULTS AND ITS STOCK
def advancedSearch(catModel, color, factory, prodYear, powerSupply):

    global advancedResults_screen
    advancedResults_screen = Tk()
    advancedResults_screen.title("Advanced Search")
    advancedResults_screen.geometry("500x620")
    advancedResults_screen.resizable(False, False)

    Label(advancedResults_screen, text="SEARCH RESULTS", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()

    catModel = catModel.get()
    color = color.get()
    factory = factory.get()
    prodYear = prodYear.get()
    powerSupply = powerSupply.get()

    query = {"PurchaseStatus": "Unsold"}

    if catModel in allCategories:
        query["Category"] = catModel
    if catModel in allModels:
        query["Model"] = catModel
    if color != "":
        query["Color"] = color
    if factory != "":
        query["Factory"] = factory    
    if prodYear != "":
        query["ProductionYear"] = prodYear
    if powerSupply != "":
        query["PowerSupply"] = powerSupply

    totalStockCount = itemsCol.find(query, {"_id": 0}).count()

    groupItems = itemsCol.aggregate([{"$match": query}, {"$group": {"_id": {"Color": "$Color", "PowerSupply": "$PowerSupply", "ProductionYear": "$ProductionYear", "Factory": "$Factory", "Product": "$Product", "Category": "$Category", "Model": "$Model"}, "Stock": {"$sum": 1}}}])

    Label(advancedResults_screen, text=totalStockCount).pack()

    scrollbar = Scrollbar(advancedResults_screen)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(advancedResults_screen, yscrollcommand = scrollbar.set, selectmode="multiple")

    groupItemData = []
    for i in groupItems:
        x = i.get("_id")

        prod = productsCol.find({"Category": str(x.get("Category")), "Model": str(x.get("Model"))})
        for p in prod:
            if (p.get("Model") == x.get("Model")) and (p.get("Category") == x.get("Category")):
                x["ProductID"] = p.get("ProductID")
                x["Warranty"] = p.get("Warranty (months)")
                x["Price"] = p.get("Price ($)")
                x["Cost"] = p.get("Cost ($)")


        mylist.insert(END, str(x.get("Category")) + ", " + str(x.get("Model")) + ", " + str(x.get("Color")) + ", $" + str(x.get("Price")) + ", " + str(x.get("Warranty")) + " Months Warranty, " + str(i.get("Stock")) + " Left")
        groupItemData.append(x)


    mylist.pack(fill = BOTH , expand= YES, padx=10, pady=10)
    scrollbar.config( command = mylist.yview )

    Button(advancedResults_screen, width=10, height=1, text="Checkout", command= lambda: checkout(groupItemData, mylist.curselection())).pack()
    Button(advancedResults_screen, width=10, height=1, text="Close", command= advancedResults_screen.destroy).pack(pady=20)

    catModelInput.delete(0, END)
    colorInput.delete(0, END)
    factoryInput.delete(0, END)
    prodYearInput.delete(0, END)
    powerSupplyInput.delete(0, END)




# ------------------------------------------ ITEM SEARCH ---------------------------------------------------------------------------------------- 
def itemSearchScreen():

    global itemSearch_screen
    itemSearch_screen = Toplevel()
    itemSearch_screen.title("Item Search")
    itemSearch_screen.geometry("300x350")
    
    Label(itemSearch_screen, text="ITEM SEARCH", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()
    Label(itemSearch_screen, text="Filter by:").pack() 


    itemID = StringVar()
    global itemIDInput

    Label(itemSearch_screen, text="ItemID * ").pack()
    itemIDInput = Entry(itemSearch_screen, textvariable=itemID)
    itemIDInput.pack()
    
    Button(itemSearch_screen, text="Search", width=10, height=1, command = lambda: [itemSearch(itemID), itemSearch_screen.destroy()]).pack()
    Button(itemSearch_screen, width=10, height=1, text="Back", command= itemSearch_screen.destroy).pack()


def itemSearch(itemID):

    global itemSearchResults_screen
    itemSearchResults_screen = Tk()
    itemSearchResults_screen.title("Item Search")
    itemSearchResults_screen.geometry("400x400")
    Label(itemSearchResults_screen, text="SEARCH RESULTS", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 20 bold").pack()

    itemID = itemID.get()
    query = {"ItemID": itemID}
    item = itemsCol.find(query, {"_id": 0})

    details = ""
    for x in item:
        details = "\nItemID: " + str(x.get("ItemID")) + "\nCategory: " + str(x.get("Category")) + "\nModel: " + str(x.get("Model")) + "\nFactory: " + str(x.get("Factory")) + "\nProductionYear: " + str(x.get("ProductionYear")) + "\nPowerSupply: " + str(x.get("PowerSupply")) + "\nColor: " + str(x.get("Color"))
        
        prod = productsCol.find({"Category": x.get("Category"), "Model": x.get("Model")}, {"_id": 0})
        for y in prod:
            details += "\nPrice: $" + str(y.get("Price ($)")) + "\nCost: $" + str(y.get("Cost ($)")) + "\nProductID: " + str(y.get("ProductID")) + "\nWarranty: " + str(y.get("Warranty (months)")) + " Months Left";
    
    Label(itemSearchResults_screen, text=details).pack()
    Button(itemSearchResults_screen, width=10, height=1, text="Close", command= itemSearchResults_screen.destroy).pack(pady=30)

    itemIDInput.delete(0, END)


# ------------------------------------------ CHECKOUT --------------------------------------------------------------------------------------------- 

def checkout(groupItemData, selection):
    cart = []

    for i in selection:
        groupType = groupItemData[i]
        cartItem = groupType
        individualItems = itemsCol.find({"Category": groupType.get("Category"), "Model": groupType.get("Model"), "ProductionYear": groupType.get("ProductionYear"), "PowerSupply": groupType.get("PowerSupply"), "Color": groupType.get("Color")}, {"_id": 0}).limit(1)
        for x in individualItems:
            cartItem["ItemID"] = x.get("ItemID")
            print(cartItem)
        cart.append(cartItem)


    for item in cart:
        # TO UPDATE UNSOLD -> SOLD IN MONGODB
        #print(item.get("ItemID"))
        itemToUpdate = {"ItemID": item.get("ItemID")}
        newValue = {"$set": { "PurchaseStatus": "Sold" }}
        # x = itemsCol.update_one(itemToUpdate, newValue) #IMPORTANT! COMMENTED OUT FOR NOW. THIS LINE ACTUALLY UPDATES BUT IDW IT NOW @@@@@@@@@@@@@@@@@
        purchase(item.get("ItemID"), item.get("Color"), item.get("Factory"), item.get("ProductionYear"), item.get("PowerSupply"), item.get("ProductID"), userID)    
    messagebox.showinfo(title="Checkout Completed!", message="Complete!")