from tkinter.constants import W
from tkinter import messagebox
from tkinter import *
import mysql.connector
    
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()    
    
def getSoldItems():

    """sql1 = "SELECT ProductID, COUNT(productID) FROM Buys LEFT JOIN Item ON productID = productID GROUP BY productID"
    mycursor.execute(sql1)
    result = mycursor.fetchall() """

    sql1 = "SELECT * FROM itemStatus"
    mycursor.execute(sql1)
    result = mycursor.fetchall()
    return result