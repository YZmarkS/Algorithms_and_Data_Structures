WITH Sells AS (
    SELECT stock_name, SUM(price) AS total
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
),
Buys AS (
    SELECT stock_name, -SUM(price) AS total
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
)
SELECT stock_name, SUM(total) AS capital_gain_loss
FROM (SELECT * FROM Sells AS S UNION SELECT * FROM Buys AS B) AS T
GROUP BY stock_name
