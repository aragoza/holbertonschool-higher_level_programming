-- count the number of recorsds that has the same score
SELECT score, COUNT(score)AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;