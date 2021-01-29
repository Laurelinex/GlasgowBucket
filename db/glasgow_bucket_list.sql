DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS zones;


CREATE TABLE zones (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    visited BOOLEAN,
    zone_id INT REFERENCES zones(id)
);