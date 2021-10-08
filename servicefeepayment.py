from datetime import date

def calculateServiceFee(requestStatus, requestDate, itemCost, requestID):

    if requestStatus == "Submitted":
        serviceFee = 0
    
    if requestStatus == "":
        serviceFee = 0

    if requestStatus == "Submitted and Waiting for payment":
        serviceFee = 40 + 0.2*itemCost

        sql = "SELECT RequestDate FROM ServiceRequest WHERE requestID = %d"
        val = [requestID]
        mycursor.execute(sql4,val4)
        myresult2 = mycursor.fetchall()

        sql1 = "SELECT paymentID FROM Payment WHERE paymentID=(SELECT max(paymentID) FROM Payment)"
        mycursor.execute(sql1)
        myresult1 = mycursor.fetchall()

        sql2 = "INSERT INTO ServiceFee (serviceFeeAmount, settledByPaymentID, creationDate, settlementDate) VALUES (%d, %d, %s, %s)"
        val2 = [serviceFee, myresult1, myresult2, ""]
    
    return serviceFee

def makeServiceFeePayment(requestID, serviceFee, paidByCustID, requestDate, requestStatus, itemCost): #button to make payment
   
    serviceFee = calculateServiceFee(requestStatus, requestDate, itemCost, requestID)

    if serviceFee != 0:
        paymentAmount = serviceFee
        paymentDate = date.today().strftime("%d/%m/%Y")

        sql = "INSERT INTO Payment (paidByCustID, paymentDate, paymentAmount) VALUES (%s, %s, %d)"
        val = [paidByCustID, paymentDate, paymentAmount]
        mycursor.execute(sql,val)
        mydb.commit()
        myresult = mycursor.fetchall()




        sql1 = "UPDATE ServiceRequest SET requestStatus = %s"
        val1 = ["In Progress"]
        mycursor.execute(sql1,val1)
        mydb.commit()

        sql2 = "UPDATE Item SET serviceStatus = %s"
        val2 = ["Waiting for approval"]
        mycursor.execute(sql2,val2)
        mydb.commit()



        ###### RYAN UPDATE MONGODB############
        ###
        #
        #
        #
        #
        #

        sql3 = "SELECT paymentID FROM Payment WHERE paymentID=(SELECT max(paymentID) FROM Payment)"
        mycursor.execute(sql3)
        myresult1 = mycursor.fetchall()

        sql4 = "SELECT RequestDate FROM ServiceRequest WHERE requestID = %d"
        val4 = [requestID]
        mycursor.execute(sql4,val4)
        myresult2 = mycursor.fetchall()

    


        sql5 = "INSERT INTO ServiceFee (serviceFeeAmount, settledByPaymentID, creationDate, settlementDate) VALUES (%d, %d, %s, %s)"
        val5 = [paymentAmount, myresult1, myresult2, paymentDate]

