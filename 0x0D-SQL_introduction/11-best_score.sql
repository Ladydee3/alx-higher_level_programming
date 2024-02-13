--list all rows of the table second_table
-- from database hbtn_0c_0
-- result display score and name
-- ordered by score
with score >= 10
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
