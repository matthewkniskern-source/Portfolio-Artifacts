-- Basic query examples from the project presentation

-- Select specific employee columns
SELECT Name, ContactInfo
FROM Employees;

-- Select all employees
SELECT *
FROM Employees;

-- Get a customer by primary key
SELECT *
FROM Customers
WHERE CustomerId = 7;

-- Review quality-control records newest first
SELECT *
FROM qualitycontrol
ORDER BY InspectionDate DESC;
