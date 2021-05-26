CREATE TABLE schemes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE residents (
    id SERIAL PRIMARY KEY,
    forename TEXT NOT NULL,
    middle_names TEXT,
    surname TEXT NOT NULL,
    dob DATE,
    previous_address TEXT,
    scheme INTEGER REFERENCES schemes(id)
);

INSERT INTO schemes (name, address) VALUES ('mandalay', 'address is not important right now 1');
INSERT INTO schemes (name, address) VALUES ('NGC', 'Nightingale Close, dont care');

CREATE TABLE opp (
    resident_id INTEGER REFERENCES residents(id) PRIMARY KEY,
    t1 TEXT NOT NULL,
    t2 TEXT NOT NULL
);

CREATE TABLE rag (
    id SERIAL PRIMARY KEY,
    colour TEXT NOT NULL
);

CREATE TABLE risks (
    id SERIAL PRIMARY KEY,
    resident_id INTEGER REFERENCES residents(id),
    risk TEXT NOT NULL,
    mitigation TEXT NOT NULL,
    rag INTEGER REFERENCES rag(id)
);

INSERT INTO rag (colour) VALUES ('green');
INSERT INTO rag (colour) VALUES ('amber');
INSERT INTO rag (colour) VALUES ('red');


CREATE TABLE sup (
    id SERIAL PRIMARY KEY,
    resident_id INTEGER REFERENCES residents(id),
    entries TEXT NOT NULL
);
