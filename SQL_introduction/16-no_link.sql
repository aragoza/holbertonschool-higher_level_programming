-- list all the rows in a table in a database
SELECT score, name
FROM second_table
WHERE NOT ISNULL(name)
ORDER BY score DESC;