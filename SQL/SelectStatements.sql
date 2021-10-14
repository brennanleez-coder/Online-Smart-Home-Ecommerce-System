CREATE DATABASE OSHES;

SELECT * from Customer;
SELECT * from Administrator;
SELECT * from Item;
SELECT * from Product;
SELECT * from Services;
SELECT * from ServiceFee;
SELECT * from ServiceRequest;
SELECT * from Buys;
SELECT * from Payment;
SELECT * from Approves;
SELECT * from Cancels;


//INSERT FOR PRESENTATION


INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (1, 10, 50, 20, "Light1", "Lights");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (2, 8, 60, 22, "Light2", "Lights");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (3, 8, 70, 30, "Light3", "Lights");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (4, 10, 100, 30, "SmartHome1", "Lights");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (5, 10, 120, 50, "Safe1", "Locks");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (6, 10, 125, 50, "Safe2", "Locks");
INSERT INTO Product (productID, warranty, price, cost, model, category) VALUES (7, 12, 200, 100, "SmartHome1", "Locks");
INSERT INTO Administrator (administratorID, fName, lName, gender, phoneNumber, password) VALUES ("A1", "ADMIN","ADMIN","123","123","123");

