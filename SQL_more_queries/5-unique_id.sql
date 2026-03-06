-- create a table where the id is always unique
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT UNIQUE AND DEFAULT 1,
    name VARCHAR(256)
);