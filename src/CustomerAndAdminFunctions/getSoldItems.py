from tkinter.constants import W
from tkinter import messagebox
from tkinter import *
import mysql.connector
    
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()    
    
def getSoldItems():
    sql = "SELECT requestID from ServiceRequest"
    mycursor.execute(sql)
    allItems = mycursor.fetchall()
    output = []
    approvedItems = []
    
    for i in allItems:

        sql1 = "SELECT requestID FROM Approves WHERE requestID = %s"
        val1 = [i[0]]
        mycursor.execute(sql1,val1)
        result = mycursor.fetchall()
        approvedItems.append(result[0])

    for i in allItems:
        if i[0] in approvedItems[0]:
            itemInfo = [approvedItems[0], "Approved"]
        else:
            itemInfo = [i[0], "Not Approved"]
        output.append(itemInfo)

    if len(output) == 0:
            messagebox.showinfo(message="No items!")
    
    return output