WITH Canonicals AS (
    SELECT MIN(id) AS canonId
    FROM Person
    GROUP BY email
)
DELETE FROM Person
WHERE Person.id NOT IN (SELECT * FROM Canonicals)
