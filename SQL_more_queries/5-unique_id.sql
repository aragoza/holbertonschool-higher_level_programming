-- create a table where the id is always unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256)
    UNIQUE (id)
);