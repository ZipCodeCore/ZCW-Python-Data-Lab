CREATE SCHEMA promarkone;
CREATE TABLE promarkone.leads
(
    id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender VARCHAR(15),
    employer VARCHAR(50),
    phone VARCHAR(15),
    tags TEXT
);
SELECT * FROM promarkone.leads;
