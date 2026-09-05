SELECT Manager.id
FROM Employee AS Manager JOIN Employee ON Manager.id = Employee.managerId
GROUP BY Manager.id
HAVING COUNT(DISTINCT Employee.id) >= 5
