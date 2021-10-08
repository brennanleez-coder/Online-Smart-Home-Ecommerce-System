
#import modules
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="OSHES"
)

#USE "OSHES"

from tkinter import *
import os
import mysql.connector
# Designing window for registration
 


def registerCustomer():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
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

 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()

    customerID_lable = Label(register_screen, text="customerID * ")
    customerID_lable.pack()
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

    #populate database
    sql = ("INSERT INTO Customer (customerID, fName, lName, gender, emailAddress, address, phoneNumber, password)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ")
    val = (customerID.get(), fName.get(), lName.get(), gender.get(), emailAddress.get(), address.get(), phoneNumber.get(), password1.get())
    
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    print('done')


    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_customer).pack()


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
    fName_entry = Entry(register_screen, textvariable=fName, show='*')
    fName_entry.pack()


    lName_lable = Label(register_screen, text="lName * ")
    lName_lable.pack()
    lName_entry = Entry(register_screen, textvariable=lName, show='*')
    lName_entry.pack()

    password2_lable = Label(register_screen, text="Password * ")
    password2_lable.pack()
    password2_entry = Entry(register_screen, textvariable=password2, show='*')
    password2_entry.pack()

    gender_lable = Label(register_screen, text="gender * ")
    gender_lable.pack()
    gender_entry = Entry(register_screen, textvariable=gender, show='*')
    gender_entry.pack()


    phoneNumber_lable = Label(register_screen, text="phoneNumber * ")
    phoneNumber_lable.pack()
    phoneNumber_entry = Entry(register_screen, textvariable=phoneNumber, show='*')
    phoneNumber_entry.pack()

    #populate database
    sql = "INSERT INTO Administrator (administratorID, fName, lName, gender, phoneNumber, password) VALUES (%s, %s, %s, %s, %s, %s) "
    val = [adminID, fName, lName, gender, emailAddress, address, phoneNumber, password2]
    mycursor.execute(sql, val)
    mydb.commit()


    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_admin).pack() """
 
 
# Designing window for login 
 
def loginCustomer():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global customerID_verify
    global password1_verify
 
    customerID_verify = StringVar()
    password1_verify = StringVar()
 
    global customerID_login_entry
    global password1_login_entry
 
    Label(login_screen, text="customerID * ").pack()
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
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
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
 
    customerID_info = customerID.get()
    password1_info = password1.get()
    gender_info = gender.get()
    emailAddress_info = emailAddress.get()
    phoneNumber_info = phoneNumber.get()
    address_info = address.get()

 

    customerID_entry.delete(0, END)
    password1_entry.delete(0, END)
    gender_entry.delete(0, END)
    emailAddress_entry.delete(0, END)
    phoneNumber_entry.delete(0, END)
    address_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()# Implementing event on register button
 
""" def register_admin():
 
    adminID_info = adminID.get()
    password2_info = password2.get()

    gender_info = gender.get()
    phoneNumber_info = phoneNumber.get()

 

    adminID_entry.delete(0, END)
    password2_entry.delete(0, END)
    gender_entry.delete(0, END)
    emailAddress_entry.delete(0, END)
    phoneNumber_entry.delete(0, END)
    address_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack() """
 
# Implementing event on login button 
 
def customerlogin_verify():
    customerUsername = customerID_verify.get()
    customerPassword = password1_verify.get()
    customerID_login_entry.delete(0, END)
    password1_login_entry.delete(0, END)
 
    sql = "SELECT customerID , password FROM Customer WHERE customerID = %s AND password = %s"
    val = [customerUsername, customerPassword]
    mycursor.execute(sql, val)
    mydb.commit()
    myresult = mycursor.fetchall()


    if myresult[0] == customerUsername:
        if myresult[1] == customerPassword:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()
 

def adminlogin_verify():
    adminUsername = adminID_verify.get()
    adminPassword = password2_verify.get()
    adminID_login_entry.delete(0, END)
    password2_login_entry.delete(0, END)
 

    sql = "SELECT administratorID , password FROM Admin WHERE administatorID = %s AND password = %s"
    val = [adminUsername, adminPassword]
    mycursor.execute(sql, val)
    mydb.commit()
    myresult = mycursor.fetchall()


    if myresult[0] == adminUsername:
        if myresult[1] == adminPassword:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_found()
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("450x500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Customer Login", height="2", width="30", command = loginCustomer).pack()
    Label(text="").pack()
    Button(text="Customer Register", height="2", width="30", command=registerCustomer).pack()
    Label(text="").pack()
    Button(text="Administrator Login", height="2", width="30", command = loginAdmin).pack()
    Label(text="").pack()
    #Button(text="Administrator Register", height="2", width="30", command=registerAdministrator).pack()
    #Label(text="").pack()
 
    main_screen.mainloop()
 

main_account_screen()