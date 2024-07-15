CREATE DATABASE exercise;
USE exercise;

CREATE TABLE employees (
  EmployeeID int NOT NULL,
  EmployeeName varchar(150) DEFAULT NULL,
  Department varchar(150) DEFAULT NULL,
  ContactNo varchar(12) DEFAULT NULL,
  Email varchar(100) DEFAULT NULL,
  AnnualSalary int DEFAULT NULL,
  PRIMARY KEY (EmployeeID)
);

INSERT INTO employees VALUES
(1, 'Seamus Hogan', 'Recruitment', '351478025', 'Seamus.h@luckyshrub.com', 50000),
(2, 'Thomas Eriksson', 'Legal', '351475058', 'Thomas.e@luckyshrub.com', 75000),
(3, 'Simon Tolo', 'Marketing', '351930582', 'Simon.t@luckyshrub.com', 40000),
(4, 'Francesca Soffia', 'Finance', '351258569', 'Francesca.s@luckyshrub.com', 45000),
(5, 'Emily Sierra', 'Customer Service', '351083098', 'Emily.s@luckyshrub.com', 35000),
(6, 'Maria Carter', 'Human Resources', '351022508', 'Maria.c@luckyshrub.com', 55000),
(7, 'Rick Griffin', 'Marketing', '351478458', 'Rick.G@luckyshrub.com', 50000);

/* Task 1: Find employees who earn an annual salary of $50,000 or more attached to the Marketing department. */
select * from employees where Department = 'Marketing' and AnnualSalary >= 50000;

/* Task 2: Find employees not earning over $50,000 across all departments. */
select * from employees where AnnualSalary <= 50000;

/* Task 3: Find Marketing, Finance, and Legal employees whose annual salary is below $50,000. */
select * from employees where Department in ('Marketing', 'Finance', 'Legal') and AnnualSalary < 50000;

/* Task 4: Find employees who earn annual salaries between $20,000 and $50,000. */
select * from employees where AnnualSalary between 20000 and 50000;

-- Task 5: Find employees whose names start with ‘S’ and are at least 4 characters in length. --
select * from employees where EmployeeName like 'S___%';



