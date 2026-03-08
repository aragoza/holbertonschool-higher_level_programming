-- create the states of the usa
CREATE DATABASES IF NOT EXISTS hbtn_0d_usa;
hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT,
    name VARCHAR(256)
);