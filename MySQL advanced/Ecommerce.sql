-- Create the Ecommerce database and switch to it
CREATE DATABASE Ecommerce;
USE Ecommerce;

-- Create Orders table
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT,
    OrderDate DATE,
    CONSTRAINT Orders_pk PRIMARY KEY (OrderID)
);

-- Create OrderItems table
CREATE TABLE OrderItems (
    OrderID INT NOT NULL,
    OrderName VARCHAR(25),
    OrderDescription VARCHAR(150),
    CONSTRAINT OrderItems_fk FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert data into Orders
INSERT INTO Orders (OrderDate) VALUES ('2025-10-12'), ('2025-08-15'), ('2025-03-13');

-- Insert data into OrderItems
INSERT INTO OrderItems (OrderID, OrderName, OrderDescription) VALUES 
(1, 'iPhone', 'This is an iPhone'),
(2, 'Honor', 'This is an Honor'),
(3, 'Vivo', 'This is a Vivo');

-- Attempting to insert an item for a non-existent order will cause an error
-- INSERT INTO OrderItems (OrderID, OrderName, OrderDescription) VALUES (4, 'Huawei', 'This is a Huawei');
-- Select all from Orders
SELECT * FROM Orders;

-- Select all from OrderItems
SELECT * FROM OrderItems;

-- Select items where OrderID = 1
SELECT * FROM OrderItems WHERE OrderID = 1;
