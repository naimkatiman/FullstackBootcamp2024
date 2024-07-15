CREATE DATABASE Pishang;
USE Pishang;

CREATE TABLE employee (
EmployeeID INT AUTO_INCREMENT NOT NULL,
EmployeeName VARCHAR(50) NOT NULL,
Department VARCHAR(15) NOT NULL,
PhoneNumber VARCHAR(12) NOT NULL,
age INT NOT NULL,	
AnnualSalary INT NOT NULL,
PRIMARY KEY (EmployeeID)         
);

INSERT INTO employee VALUES
(1,"Jebon","Admin",0121321322,23,800000),
(2,"Jojo","CS",01942121434,25,400000),
(3,"John","Finance",01992322113,25,300000),
(4,"Juan","Legal",01941241,28,300000),
(5,"Jalin","Finance",0199934,37,600000),
(6,"Jem","Marketing",019123122,26,400000),
(7,"JJ","IT",019993443,26,600000);

/* Query */

SELECT * FROM employee;
SELECT * FROM employee where EmployeeID=2;
SELECT * FROM employee where AnnualSalary >= 500000;
SELECT * FROM employee where AnnualSalary between 300000 AND 500000;
SELECT * FROM employee where Department = 'Finance' AND AnnualSalary > 500000;
SELECT AVG(AnnualSalary) from employee;

/* Return all employee from employee department that start with the letter 'L':*/

SELECT * FROM employee where Department LIKE 'L%';
SELECT * FROM employee where Department like '%N';
SELECT EmployeeName AS stuff from employee;
SELECT EmployeeName from employee;
SELECT * FROM employee where AnnualSalary >= 500000 AND Department = 'Finance';

/* TAsk Use the BETWEEN operators to find employees who earn annual salaries between 300000 and 600000 */

SELECT 
    *
FROM
    employee
WHERE
    AnnualSalary BETWEEN 300000 AND 600000;
    
show tables;
    
 /* Task 2: Use the AND Operator to find employee not earning over 500000 across marketing and cs departments. */   
 
 /* IN */ 
 
    
SELECT * FROM employee
WHERE AnnualSalary <= 500000
AND Department IN ('Marketing', 'CS');
