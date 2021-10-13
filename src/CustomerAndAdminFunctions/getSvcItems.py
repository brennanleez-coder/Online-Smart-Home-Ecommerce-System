from tkinter.constants import W
from tkinter import messagebox
from tkinter import *
import mysql.connector
    
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()    
    
def getServiceItems():

    output = []
    ### RETURNS ALL THOSE WHO SUBMITTED SERVICE REQUEST THAT IS NOT APPROVED OR CANCELLED
    # myresult (requestID, itemID, customerId, requestStatus, requestDate)
    sql = "SELECT requestID, requestStatus FROM ServiceRequest WHERE requestStatus = %s OR requestStatus = %s OR requestStatus = %s"
    val = ["Submitted", "In Progress", "Approved"]
    mycursor.execute(sql,val)
    result = mycursor.fetchall()

    if len(result) > 0:
        for i in result:
            output.append(i)

    if len(output) == 0:
            messagebox.showinfo(message="Nothing in Service!")

    return output