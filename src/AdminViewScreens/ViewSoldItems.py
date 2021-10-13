from tkinter import *
import os
import mysql.connector
from CustomerAndAdminFunctions.getSoldItems import getSoldItems

mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def viewSoldItemsScreen():

    output = getSoldItems()

    global soldItems_screen
    soldItems_screen = Tk()
    soldItems_screen.geometry("300x330")
    soldItems_screen.resizable(False, False)

    soldItems_screen.title("Sold Items")
    Label(soldItems_screen,text="SOLD ITEMS",fg='Gold', bg='Maroon', width="300", height="3", font = "Helvetica 20 bold").pack(anchor=NE)
    # CAN LIST OUT ALL ITEMIDS THAT ARE SOLD. QUERY HERE.

    ##category counter##
    LightsCount = 0;
    LocksCount = 0
    
    ##model counter##
    Light1 = 0
    Light2 = 0
    SmartHome1Count = 0
    Safe1 = 0
    Safe2 = 0
    Safe3 = 0 
    
    LightsID = ["001","002", "003"]
    LocksID = ["004","005","006","007"]
    # output is a list of tuples
    for item in output:

        print(item)
        if item[0] in LightsID:
            LightsCount += item[1]
            if item[0] == "001":
                Light1 += item[1]
            elif item[0] == "002":
                Light2 += item[1]
            elif item[0] == "003":
                SmartHome1Count += item[1]
        if item[0] in LocksID:
            LocksCount += item[1]
            if item[0] == "004":
                Safe1 += item[1]
            elif item[0] == "005":
                Safe2 += item[1]
            elif item[0] == "006":
                Safe3 += item[1]
            elif item[0] == "007":
                SmartHome1Count += item[1]



    Label(soldItems_screen,text= "Lights Count: " + str(LightsCount)).pack(anchor= N)
    Label(soldItems_screen,text= "Locks Count: " + str(LocksCount)).pack(anchor= N)
    Label(soldItems_screen,text= "Light1 Count: " + str(Light1)).pack(anchor= N)
    Label(soldItems_screen,text= "Light2 Count: " + str(Light2)).pack(anchor= N)
    Label(soldItems_screen,text= "Safe1 Count: " + str(Safe1)).pack(anchor= N)
    Label(soldItems_screen,text= "Safe2 Count: " + str(Safe2)).pack(anchor= N)
    Label(soldItems_screen,text= "Safe3 Count: " + str(Safe3)).pack(anchor= N)
    Label(soldItems_screen,text= "SmartHome1 Count: " + str(SmartHome1Count)).pack(anchor= N)
