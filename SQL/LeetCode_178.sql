WITH ScoreRank AS (
    SELECT score, ROW_NUMBER() OVER(ORDER BY score DESC) AS `rank`
    FROM Scores
    GROUP BY score
)
SELECT Scores.score, `rank`
FROM Scores JOIN ScoreRank ON Scores.score = ScoreRank.score
ORDER BY Scores.score DESC
