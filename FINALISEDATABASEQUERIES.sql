CREATE TABLE Customer (
    customerID VARCHAR(100) NOT NULL,
    fName VARCHAR(50),
    lName VARCHAR(50),
    Gender VARCHAR(10),
    emailAddress VARCHAR(255),
    address VARCHAR(255),
    phoneNumber VARCHAR(50),
    password VARCHAR(255),
    PRIMARY KEY (customerID)
);


CREATE TABLE Administrator (
    administratorID VARCHAR(100) NOT NULL ,
	fName VARCHAR(255),
    lName VARCHAR(255),
    Gender VARCHAR(10),
    phoneNumber VARCHAR(50),
    password VARCHAR(255),
    PRIMARY KEY (administratorID)
);




CREATE TABLE Item (
    itemID INT(4) NOT NULL,
    purchaseStatus VARCHAR(50),
    powerSupply VARCHAR(50),
    factory VARCHAR(255),
    productionYear VARCHAR(50),
    colour VARCHAR(10),
    productID INT(2),
    PRIMARY KEY (itemID)
);

CREATE TABLE Product (
    productID INT(2),
    warranty INT(2),
    price INT(3),
    cost INT(3),
    model VARCHAR(10),
    category VARCHAR(10),
    PRIMARY KEY (productID),
	FOREIGN KEY (productID) REFERENCES Item(productID)
    
);

CREATE TABLE Services(
	serviceID INT(20) NOT NULL AUTO_INCREMENT,
    serviceStatus VARCHAR(50),
    servicedByAdminID VARCHAR(100),
    itemID INT(4),
    
    PRIMARY KEY (itemID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    FOREIGN KEY (servicedByAdminID) REFERENCES Administrator(administratorID)
);

CREATE TABLE ServiceRequest (
    requestID INT(20) NOT NULL AUTO_INCREMENT,
    requestDate DATE,
    createdByCustID VARCHAR(100),
    requestStatus VARCHAR(50),
    
    PRIMARY KEY (requestID),
    FOREIGN KEY (createdByCustID)
        REFERENCES Customer (customerID)
);

CREATE TABLE Payment (
    paymentID INT(20) NOT NULL AUTO_INCREMENT,
    paidByCustID VARCHAR(100),
    paymentAmount INT(20),
    paymentDate DATE,
    PRIMARY KEY (paymentID),
	CONSTRAINT payment_ibfk_1 FOREIGN KEY (paidByCustID)
        REFERENCES Customer (customerID)
);


CREATE TABLE ServiceFee (
    requestID INT(20),
    serviceFeeAmount INT(4),
    creationDate DATE,
    settlementDate DATE,
    settledByPaymentID INT(20),
    PRIMARY KEY (requestID, serviceFeeAmount),
    FOREIGN KEY (settledByPaymentID)
        REFERENCES Payment (paymentID),
	FOREIGN KEY (requestID) REFERENCES ServiceRequest(requestID)
);


CREATE TABLE Cancels (
	requestID INT(20),
    cancellationDate DATE,
    cancelledByCustID VARCHAR(100),
    PRIMARY KEY (cancelledByCustID),
    FOREIGN KEY (cancelledByCustID) REFERENCES Customer(customerID),
    FOREIGN KEY (requestID) REFERENCES ServiceRequest(requestID)
);


CREATE TABLE Buys (
	itemID INT(4) NOT NULL,
	purchasedByCustID VARCHAR(100),
	purchaseDate DATE,
    PRIMARY KEY (itemID),
	FOREIGN KEY (puchasedByCustID) REFERENCES Customer(customerID)
);


CREATE TABLE Approves (
	approvedByAdminID VARCHAR(100),
    requestID INT(20),
    approvalDate DATE,
    PRIMARY KEY (requestID),
    FOREIGN KEY (approvedByAdminID)
        REFERENCES Administrator (administratorID)
);