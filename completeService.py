from datetime import date
from tkinter import messagebox
from tkinter import *
import os
import mysql.connector
# Designing window for approval
 
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def completeService():

    sql = "UPDATE ServiceRequest SET requestStatus = %s"
    val = ["Completed"]
    mycursor.execute(sql,val)
    mydb.commit()

    sql1 = "UPDATE Services SET serviceStatus = %s"
    val1 = ["Completed"]
    mycursor.execute(sql1,val1)
    mydb.commit()

