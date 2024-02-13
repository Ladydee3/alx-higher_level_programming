-- create a table first_table in current db
-- does not fail if table exits
CREATE TABLE IF NOT EXITS first_table (id INT,
name VARCHAR(256));
