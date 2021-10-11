
#import modules
 
from tkinter import *
import os
import mysql.connector
from CustomerView import customerview
from AdminView import adminview

# Designing window for registration
 
mydb = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='OSHES')

mycursor = mydb.cursor()

def registerCustomer():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x600")
    register_screen.resizable(False, False)

 
    global customerID
    global fName
    global lName
    global password1
    global gender
    global emailAddress
    global phoneNumber
    global address

    global address_entry
    global customerID_entry
    global fName_entry
    global lName_entry
    global password1_entry
    global phoneNumber_entry
    global emailAddress_entry
    global gender_entry
   
    customerID = StringVar()
    fName = StringVar()
    lName = StringVar()
    password1 = StringVar()
    gender = StringVar()
    emailAddress = StringVar()
    phoneNumber = StringVar()
    address = StringVar() 

 
    Label(register_screen, text="REGISTRATION", fg="White", bg="Maroon", width="300", height="3", font = "Helvetica 20 bold").pack()
    Label(register_screen, text="").pack()

    customerID_lable = Label(register_screen, text="customerID * ")
    customerID_lable.pack()
    customerID_lable2 = Label(register_screen, text="(ENTER DIGITS ONLY)")
    customerID_lable2.pack()

    customerID_entry = Entry(register_screen, textvariable=customerID)
    customerID_entry.pack()

    password1_lable = Label(register_screen, text="Password * ")
    password1_lable.pack()
    password1_entry = Entry(register_screen, textvariable=password1, show='*')
    password1_entry.pack()

    fName_lable = Label(register_screen, text="fName * ")
    fName_lable.pack()
    fName_entry = Entry(register_screen, textvariable=fName)
    fName_entry.pack()


    lName_lable = Label(register_screen, text="lName * ")
    lName_lable.pack()
    lName_entry = Entry(register_screen, textvariable=lName)
    lName_entry.pack()

    gender_lable = Label(register_screen, text="gender * ")
    gender_lable.pack()
    gender_entry = Entry(register_screen, textvariable=gender)
    gender_entry.pack()

    emailAddress_lable = Label(register_screen, text="emailAddress * ")
    emailAddress_lable.pack()
    emailAddress_entry = Entry(register_screen, textvariable=emailAddress)
    emailAddress_entry.pack()

    phoneNumber_lable = Label(register_screen, text="phoneNumber * ")
    phoneNumber_lable.pack()
    phoneNumber_entry = Entry(register_screen, textvariable=phoneNumber)
    phoneNumber_entry.pack()

    address_lable = Label(register_screen, text="address * ")
    address_lable.pack()
    address_entry = Entry(register_screen, textvariable=address)
    address_entry.pack()



    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_customer).pack()

 
# Designing window for login 
 
def loginCustomer():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    login_screen.resizable(False, False)

    Label(login_screen, text="LOGIN AS CUSTOMER", fg="Gold", bg="Maroon", width="300", height="3", font = "Helvetica 16 bold").pack()
    Label(login_screen, text="").pack()
 
    global customerID_verify
    global password1_verify
 
    customerID_verify = StringVar()
    password1_verify = StringVar()
 
    global customerID_login_entry
    global password1_login_entry
 

    Label(login_screen, text="customerID * ").pack()
    Label(login_screen, text="(ENTER DIGITS ONLY)").pack()

    customerID_login_entry = Entry(login_screen, textvariable=customerID_verify)
    customerID_login_entry.pack()

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password1_login_entry = Entry(login_screen, textvariable=password1_verify, show= '*')
    password1_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = customerlogin_verify).pack()

def loginAdmin():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    login_screen.resizable(False, False)

    Label(login_screen, text="LOGIN AS ADMIN", fg="Gold", bg="Maroon", width="300", height="3", font = "Helvetica 16 bold").pack()
    Label(login_screen, text="").pack()
 
    global adminID_verify
    global password2_verify
 
    adminID_verify = StringVar()
    password2_verify = StringVar()
 
    global adminID_login_entry
    global password2_login_entry
 
    Label(login_screen, text="adminID * ").pack()
    adminID_login_entry = Entry(login_screen, textvariable=adminID_verify)
    adminID_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password2_login_entry = Entry(login_screen, textvariable=password2_verify, show= '*')
    password2_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = adminlogin_verify).pack()
 
# Implementing event on register button
 
def register_customer():
 
    customerID_info = customerID_entry.get()
    password1_info = password1_entry.get()
    gender_info = gender_entry.get()
    emailAddress_info = emailAddress_entry.get()
    phoneNumber_info = phoneNumber_entry.get()
    address_info = address_entry.get()

    #populate database
    sql = ("INSERT INTO Customer (customerID, fName, lName, gender, emailAddress, address, phoneNumber, password)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ")
    val = (customerID_entry.get(), fName_entry.get(), lName_entry.get(), gender_entry.get(), emailAddress_entry.get(), address_entry.get(), phoneNumber_entry.get(), password1_entry.get())
    mycursor.execute(sql, val)
    mydb.commit()

    customerID_entry.delete(0, END)
    fName_entry.delete(0, END)
    lName_entry.delete(0, END)
    password1_entry.delete(0, END)
    gender_entry.delete(0, END)
    emailAddress_entry.delete(0, END)
    phoneNumber_entry.delete(0, END)
    address_entry.delete(0, END) 
 
    Label(register_screen, text="Registration Success", fg="Gold", font=("calibri", 11)).pack()# Implementing event on register button
 
# Implementing event on login button 
 
def customerlogin_verify():
    customerUsername = customerID_verify.get()
    customerPassword = password1_verify.get()
    customerID_login_entry.delete(0, END)
    password1_login_entry.delete(0, END)
 
    sql = ("SELECT customerID , password FROM Customer WHERE customerID = %s AND password = %s")
    val = (customerUsername, customerPassword)
    mycursor.execute(sql, val)
    #mydb.commit()
    myresult = mycursor.fetchall()

    if len(myresult) == 1:
        login_sucess("customer")
    else:
        user_not_found()


def adminlogin_verify():
    adminUsername = adminID_verify.get()
    adminPassword = password2_verify.get()
    adminID_login_entry.delete(0, END)
    password2_login_entry.delete(0, END)
 
    sql = ("SELECT administratorID , password FROM Administrator WHERE administratorID = %s AND password = %s")
    val = (adminUsername, adminPassword)
    mycursor.execute(sql, val)
    #mydb.commit()
    myresult = mycursor.fetchall()

    if len(myresult) == 1:
        login_sucess("admin")
    else:
        user_not_found()

# Designing popup for login success
 
def login_sucess(loginType):
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x90")
    main_screen.resizable(False, False)

    Label(login_success_screen, text="Login Successfully!").pack(pady=10, padx=5)
    if loginType == "customer":
        Button(login_success_screen, text="OK", command=lambda:[delete_login_success(), customerview()]).pack()
    else:
        Button(login_success_screen, text="OK", command=lambda:[delete_login_success(), adminview()]).pack()


# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("210x90")
    user_not_found_screen.resizable(False, False)

    Label(user_not_found_screen, text="Wrong Username / Password!").pack(pady=10, padx=5)
    Button(user_not_found_screen, text="OK", command=user_not_found_screen.destroy).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()

# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("700x500")
    main_screen.title("OSHES")
    main_screen.resizable(False, False)

    img = PhotoImage(file="img/1.png")
    label = Label(main_screen,image=img)
    label.place(x=0, y=25)


    Label(text="Online Smart Home Ecommerce System", fg="Gold", bg="Maroon", width="300", height="4", font = "Helvetica 28 bold").pack()
    custLogin = Button(text="Customer Login", height="2", width="30", command = loginCustomer)
    custLogin.place(relx=0.3,rely=0.42)

    custRegister = Button(text="Customer Register", height="2", width="30", command=registerCustomer)
    custRegister.place(relx=0.3,rely=0.52)

    adminLogin = Button(text="Administrator Login", height="2", width="30", command = loginAdmin)
    adminLogin.place(relx=0.3,rely=0.62)

 
    addInfo = Label(text="© BT2102 GROUP 6.", font = "Helvetica 12 italic")
    addInfo.place(relx=0.7,rely=0.9)

    main_screen.mainloop()
 

main_account_screen()









""" def registerAdministrator():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global adminID
    global fName
    global lName
    global password2
    global gender
    global phoneNumber

    global adminID_entry
    global fName_entry
    global lName_entry
    global password2_entry
    global phoneNumber_entry

    global gender_entry
   
    adminID = StringVar()
    fName = StringVar()
    lName = StringVar()
    password2 = StringVar()
    gender = StringVar()
    emailAddress = StringVar()
    phoneNumber = StringVar()
    address = StringVar()  

 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    adminID_lable = Label(register_screen, text="adminID * ")
    adminID_lable.pack()
    adminID_entry = Entry(register_screen, textvariable=adminID)
    adminID_entry.pack()

    fName_lable = Label(register_screen, text="fName * ")
    fName_lable.pack()
    fName_entry = Entry(register_screen, textvariable=fName)
    fName_entry.pack()


    lName_lable = Label(register_screen, text="lName * ")
    lName_lable.pack()
    lName_entry = Entry(register_screen, textvariable=lName)
    lName_entry.pack()

    password2_lable = Label(register_screen, text="Password * ")
    password2_lable.pack()
    password2_entry = Entry(register_screen, textvariable=password2, show='*')
    password2_entry.pack()

    gender_lable = Label(register_screen, text="gender * ")
    gender_lable.pack()
    gender_entry = Entry(register_screen, textvariable=gender)
    gender_entry.pack()


    phoneNumber_lable = Label(register_screen, text="phoneNumber * ")
    phoneNumber_lable.pack()
    phoneNumber_entry = Entry(register_screen, textvariable=phoneNumber)
    phoneNumber_entry.pack()


    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, command = register_admin).pack()
  
def register_admin():
 
    adminID_info = adminID.get()
    password2_info = password2.get()

    gender_info = gender.get()
    phoneNumber_info = phoneNumber.get()

    #populate database
    sql = ("INSERT INTO Administrator (administratorID, fName, lName, gender, phoneNumber, password) VALUES (%s, %s, %s, %s, %s, %s) ")
    val = (adminID_entry.get(), fName_entry.get(), lName_entry.get(), gender_entry.get(), phoneNumber_entry.get(), password2_entry.get())
    mycursor.execute(sql, val)
    mydb.commit()

    adminID_entry.delete(0, END)
    password2_entry.delete(0, END)
    gender_entry.delete(0, END)
    fName_entry.delete(0, END)
    lName_entry.delete(0, END)
    phoneNumber_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
  """