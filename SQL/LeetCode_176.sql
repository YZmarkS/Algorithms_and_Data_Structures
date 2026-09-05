SELECT MAX(salary) as SecondHighestSalary
FROM (
     SELECT DISTINCT salary
     FROM Employee
     ORDER BY salary DESC
     LIMIT 1, 1
     ) as Temp
