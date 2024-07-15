CREATE DATABASE Excercise2;
USE Exercise2;

CREATE TABLE Employee (
  EmployeeId INT PRIMARY KEY,
  FullName VARCHAR(45) NOT NULL,
  Department VARCHAR(45) NOT NULL,
  Salary FLOAT NOT NULL,
  Gender VARCHAR(45) NOT NULL,
  Age INT NOT NULL
);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1001, 'John Doe', 'IT', 35000, 'Male', 25);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1002, 'Mary Smith', 'HR', 45000, 'Female', 27);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1003, 'James Brown', 'Finance', 50000, 'Male', 28);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1004, 'Mike Walker', 'Finance', 50000, 'Male', 28);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1005, 'Linda Jones', 'HR', 75000, 'Female', 26);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1006, 'Anurag Mohanty', 'IT', 35000, 'Male', 25);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1007, 'Priyanla Dewangan', 'HR', 45000, 'Female', 27);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1008, 'Sambit Mohanty', 'IT', 50000, 'Male', 28);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1009, 'Pranaya Kumar', 'IT', 50000, 'Male', 28);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1010, 'Hina Sharma', 'HR', 75000, 'Female', 26);
INSERT INTO Employee (EmployeeId, FullName, Department, Salary, Gender, Age) VALUES (1015, 'Hina ', 'software dev', 75000, 'Male', 25);

CREATE TABLE Projects (
    ProjectId INT PRIMARY KEY AUTO_INCREMENT,
    ProjectName VARCHAR(200) NOT NULL,
	EmployeeId INT,
    StartDate DATETIME,
    EndDate DATETIME,
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
);

INSERT INTO Projects (ProjectName, EmployeeId, StartDate, EndDate) VALUES 
('Develop Ecommerse Website from scratch', 1003, NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY)),
('WordPress Website for our company', 1002, NOW(), DATE_ADD(NOW(), INTERVAL 45 DAY)),
('Manage our Company Servers', 1007, NOW(), DATE_ADD(NOW(), INTERVAL 45 DAY)),
('Hosting account is not working', 1009, NOW(), DATE_ADD(NOW(), INTERVAL 7 DAY)),
('MySQL database from my desktop application', 1010, NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY)),
('Develop new WordPress plugin for my business website', NULL, NOW(), DATE_ADD(NOW(), INTERVAL 10 DAY)),
('Migrate web application and database to new server', NULL, NOW(), DATE_ADD(NOW(), INTERVAL 5 DAY)),
('Android Application development', 1004, NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY)),
('Hosting account is not working', 1001, NOW(), DATE_ADD(NOW(), INTERVAL 7 DAY)),
('MySQL database from my desktop application', 1008, NOW(), DATE_ADD(NOW(), INTERVAL 15 DAY)),
('Develop new WordPress plugin for my business website', NULL, NOW(), DATE_ADD(NOW(), INTERVAL 10 DAY));


select * from  Projects;

CREATE TABLE Address
(
    AddressId INT PRIMARY KEY AUTO_INCREMENT,
    EmployeeId INT,
    Country VARCHAR(50),
    State VARCHAR(50),
    City VARCHAR(50),
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
);
-- add column --
alter table Address add column PostCode int;

-- delete column --
alter table Adress drop column PostCode;

-- modify --
alter table Address modify PostCode varchar(50);

describe Address;



INSERT INTO Address (EmployeeId, Country, State, City) Values (1001, 'India', 'Odisha', 'BBSR');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1002, 'India', 'Maharashtra', 'Mumbai');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1003, 'India', 'Maharashtra', 'Pune');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1004, 'India', 'Odisha', 'Cuttack');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1005, 'India', 'Maharashtra', 'Nagpur');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1006, 'India', 'Odisha', 'Cuttack');
INSERT INTO Address (EmployeeId, Country, State, City) Values (1015, 'Malaysia', 'Selangor', 'Setapak');

/*  retrieve all the EmployeeId, FullName, Department, Gender, ProjectName from the Employee and Projects tables where the gender is Male. The following is the SQL Script.*/

select Employee.EmployeeId, FullName, Department, Gender, ProjectName
from Employee 
join Projects  on Employee.EmployeeId = Projects.EmployeeId
where Employee.Gender = 'Male';

-- Retrieve the Count of employeeID and using GROUP operator by gender from employee table --

select Gender, count(EmployeeId) as EmployeeCount
from Employee
group by Gender;

/* Use the AND operator to find employees who earn an salary of 40,000 or more attached to the IT department*/

select * from Employee
where Salary >= 40000
and Department = 'IT';

/*Return all employe from a employees departemnt that contains the letter 'R' :*/

select * from Employee
where Department like '%R%';

/* Use the BETWEEN operator to find employees who earn salaries between $40,000 and $60,000. */

select * from Employee
where Salary between 40000 and 60000;