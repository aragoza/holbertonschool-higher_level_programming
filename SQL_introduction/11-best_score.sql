-- display the score above 10 from the best to the worst
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;