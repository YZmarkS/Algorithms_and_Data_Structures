WITH SalaryPerDepartment AS (
    SELECT Department.id, Department.name, MAX(Employee.salary) AS maxSalary
    FROM Department JOIN Employee ON Department.id = Employee.departmentId
    GROUP BY Department.id
)
SELECT
    SalaryPerDepartment.name AS Department,
    Employee.name AS Employee,
    Employee.salary AS Salary
FROM Employee JOIN SalaryPerDepartment
ON Employee.departmentId = SalaryPerDepartment.id
WHERE Employee.salary = maxSalary
