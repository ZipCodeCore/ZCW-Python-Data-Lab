CREATE SCHEMA promarkone;
CREATE TABLE promarkone.leads
(
    lead_id VARCHAR(36) PRIMARY KEY NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender VARCHAR(15),
    employer VARCHAR(50),
    phone VARCHAR(15)
);
CREATE TABLE promarkone.tags
(
    tag_id VARCHAR(36) PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL
);
CREATE TABLE promarkone.lead_tag
(
    lead_id VARCHAR(36) NOT NULL,
    tag_id VARCHAR(36) NOT NULL
);
