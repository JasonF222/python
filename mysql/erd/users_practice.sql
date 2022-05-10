USE users_schema;
SELECT * FROM users;
INSERT INTO users (first_name, last_name) VALUES ('Tony', 'Stark');
INSERT INTO users (first_name, last_name) VALUES ('Barbara', 'Walters');
INSERT INTO users (first_name, last_name) VALUES ('Betty', 'White');

UPDATE users SET email = 'tstark@email.com' WHERE id = 1;
UPDATE users SET email = 'bwalters@email.com' WHERE id = 2;
UPDATE users SET email = 'bwhite@email.com' WHERE id = 3;
SELECT * FROM  users;

SELECT email FROM users WHERE id = 1;

SELECT id FROM users WHERE id = 3;

UPDATE users SET last_name = 'Pancakes' WHERE id = 3;

DELETE FROM users WHERE id = 2;
DELETE FROM users WHERE id = 5;
DELETE FROM users WHERE id = 4;
DELETE FROM users WHERE id = 6;

SELECT * FROM users ORDER BY first_name;