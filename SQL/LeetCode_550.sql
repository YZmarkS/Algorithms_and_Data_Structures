FirstLogin AS (
    SELECT player_id, MIN(event_date) AS created
    FROM Activity
    GROUP BY player_id
),
ReturningPlayers AS (
    SELECT FirstLogin.player_id
    FROM FirstLogin JOIN Activity
    ON
        FirstLogin.player_id = Activity.player_id AND
        DATE_ADD(FirstLogin.created, INTERVAL 1 DAY) = Activity.event_date
),
PlayerCount AS (
    SELECT COUNT(*) AS total FROM FirstLogin
),
ReturningCount AS (
    SELECT COUNT(*) AS sub FROM ReturningPlayers
)
SELECT ROUND(sub / total, 2) AS fraction FROM PlayerCount, ReturningCount
