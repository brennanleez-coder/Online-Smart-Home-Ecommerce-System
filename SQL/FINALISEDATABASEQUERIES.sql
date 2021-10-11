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
    itemID VARCHAR(4) NOT NULL,
    model VARCHAR(10),
    category VARCHAR(10),
    purchaseStatus VARCHAR(50),
    powerSupply VARCHAR(50),
    factory VARCHAR(255),
    productionYear VARCHAR(50),
    colour VARCHAR(10),
    PRIMARY KEY (itemID)
);

CREATE TABLE Product (
    productID INT UNIQUE NOT NULL,
    warranty INT,
    price INT,
    cost INT,
    PRIMARY KEY (productID)
);

CREATE TABLE Services(
	serviceID INT NOT NULL AUTO_INCREMENT,
    serviceStatus VARCHAR(50),
    servicedByAdminID VARCHAR(100),
    itemID VARCHAR(4),
    PRIMARY KEY (serviceID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    FOREIGN KEY (servicedByAdminID) REFERENCES Administrator(administratorID)
);

CREATE TABLE ServiceRequest (
    requestID INT NOT NULL AUTO_INCREMENT,
    itemID VARCHAR(4) NOT NULL,
    requestDate DATE,
    createdByCustID VARCHAR(100),
    requestStatus VARCHAR(50),
    
    PRIMARY KEY (requestID),
    FOREIGN KEY (createdByCustID)
	REFERENCES Customer (customerID),
	FOREIGN KEY (itemID) REFERENCES Item (itemID)
);

CREATE TABLE Payment (
    paymentID INT NOT NULL AUTO_INCREMENT,
    paidByCustID VARCHAR(100),
    paymentAmount INT,
    paymentDate DATE,
    PRIMARY KEY (paymentID),
	CONSTRAINT payment_ibfk_1 FOREIGN KEY (paidByCustID)
        REFERENCES Customer (customerID)
);


CREATE TABLE ServiceFee (
    requestID INT,
    serviceFeeAmount INT,
    creationDate DATE,
    settlementDate DATE,
    settledByPaymentID INT,
    PRIMARY KEY (requestID, serviceFeeAmount),
    FOREIGN KEY (settledByPaymentID)
        REFERENCES Payment (paymentID),
	FOREIGN KEY (requestID) REFERENCES ServiceRequest(requestID)
);


CREATE TABLE Cancels (
	requestID INT,
    cancellationDate DATE,
    cancelledByCustID VARCHAR(100),
    PRIMARY KEY (cancelledByCustID),
    FOREIGN KEY (cancelledByCustID) REFERENCES Customer(customerID),
    FOREIGN KEY (requestID) REFERENCES ServiceRequest(requestID)
);


CREATE TABLE Buys (
	itemID VARCHAR(4) NOT NULL,
	purchasedByCustID VARCHAR(100),
	purchaseDate DATE,
    PRIMARY KEY (itemID),
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
	FOREIGN KEY (purchasedByCustID) REFERENCES Customer(customerID)
);


CREATE TABLE Approves (
	approvedByAdminID VARCHAR(100),
    requestID INT,
    approvalDate DATE,
    PRIMARY KEY (requestID),
    FOREIGN KEY (approvedByAdminID)
        REFERENCES Administrator (administratorID)
);