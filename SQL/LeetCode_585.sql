WITH AlonePid AS (
    SELECT MAX(pid) AS pid
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
, NonUnique2015 AS (
    SELECT MAX(tiv_2015) AS tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
, Rounded AS (
    SELECT ROUND(tiv_2016, 2) AS `values`
    FROM Insurance
    JOIN AlonePid ON Insurance.pid = AlonePid.pid
    JOIN NonUnique2015 ON Insurance.tiv_2015 = NonUnique2015.tiv_2015
)
SELECT ROUND(SUM(`values`), 2) AS tiv_2016
FROM Rounded
