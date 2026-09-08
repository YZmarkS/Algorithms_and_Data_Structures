WITH RankingWithinDepartment AS (
    SELECT name, salary, DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rnk, departmentId
    FROM Employee
)
SELECT D.name AS Department, R.name AS Employee, R.salary AS Salary
FROM RankingWithinDepartment AS R
JOIN Department AS D ON R.departmentId = D.id
WHERE R.rnk <= 3
