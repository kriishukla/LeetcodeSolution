SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT OUTER JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;
