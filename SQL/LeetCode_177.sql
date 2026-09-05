CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
       WITH UniqueSalary AS (
       	    SELECT DISTINCT salary
	    FROM Employee
	    ORDER BY salary DESC
	    ),
      SalaryToRowNum AS (
            SELECT salary, ROW_NUMBER() OVER() AS rowNum
	    FROM UniqueSalary
      )
      SELECT salary
      FROM SalaryToRowNum
      WHERE rowNum = N
  );
END
