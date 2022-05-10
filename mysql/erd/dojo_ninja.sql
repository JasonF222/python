USE dojos_and_ninjas;

INSERT INTO dojos (name, created_at, updated_at) VALUES ('Kintsuki', now(), now());
INSERT INTO dojos (name, created_at, updated_at) VALUES ('Sasuki', now(), now());
INSERT INTO dojos (name, created_at, updated_at) VALUES ('Dojitsu', now(), now());

SET SQL_SAFE_UPDATES = 0;

DELETE FROM dojos WHERE name = 'Kintsuki';
DELETE FROM dojos WHERE name = 'Sasuki';
DELETE FROM dojos WHERE name = 'Dojitsu';

INSERT INTO dojos (id, name, created_at, updated_at) VALUES (1, 'Kintsuki', now(), now());
INSERT INTO dojos (id, name, created_at, updated_at) VALUES (2, 'Sasuki', now(), now());
INSERT INTO dojos (id, name, created_at, updated_at) VALUES (3, 'Dojitsu', now(), now());

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Naruto' , 'Uzumaki' , 15, 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Sasuke' , 'Uchiha' , 15, 1);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Kakashi' , 'Sesei' , 32, 1);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Barry' , 'White' , 45, 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Marvin' , 'Gay' , 45, 2);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Usher' , 'Rain' , 45, 2);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Taco' , 'Cat' , 15, 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Burrito' , 'Dog' , 15, 3);
INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ('Nacho' , 'Fish' , 15, 3);

SELECT * FROM ninjas WHERE dojo_id = 1;

SELECT * FROM ninjas WHERE dojo_id = (SELECT MAX(id) FROM dojos);

SELECT * FROM dojos WHERE id = (SELECT dojo_id FROM ninjas WHERE id = (SELECT MAX(id) FROM ninjas));