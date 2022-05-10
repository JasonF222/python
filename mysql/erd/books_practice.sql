USE books;

INSERT INTO authors (name) VALUES ('Jane Austin');
INSERT INTO authors (name) VALUES ('Emily Dickinson');
INSERT INTO authors (name) VALUES ('Fyodor Dostoevsky');
INSERT INTO authors (name) VALUES ('William Shakespeare');
INSERT INTO authors (name) VALUES ('Lau Tzu');

INSERT INTO books (title, num_of_pages) VALUES ('C SHARP', 473);
INSERT INTO books (title, num_of_pages) VALUES ('Java', 669);
INSERT INTO books (title, num_of_pages) VALUES ('Python', 569);
INSERT INTO books (title, num_of_pages) VALUES ('PHP', 425);
INSERT INTO books (title, num_of_pages) VALUES ('Ruby', 150);

UPDATE books SET title = 'C#' WHERE id = 1;

UPDATE authors SET name = 'Bill Shakespeare' WHERE id = 4;

INSERT INTO favorites (author_id, book_id) VALUES (1, 1);
INSERT INTO favorites (author_id, book_id) VALUES (1, 2);

INSERT INTO favorites (author_id, book_id) VALUES (2, 1);
INSERT INTO favorites (author_id, book_id) VALUES (2, 2);
INSERT INTO favorites (author_id, book_id) VALUES (2, 3);

INSERT INTO favorites (author_id, book_id) VALUES (3, 1);
INSERT INTO favorites (author_id, book_id) VALUES (3, 2);
INSERT INTO favorites (author_id, book_id) VALUES (3, 3);
INSERT INTO favorites (author_id, book_id) VALUES (3, 4);

-- UPDATE favorites SET author_id = 3 WHERE book_id IN(1, 2, 3, 4); -- another way of doing the above 4 entries
-- UPDATE favorites SET author_id = 3 WHERE book_id BETWEEN 1 AND 5; -- ANOTHER way of doing the above 4 entries

INSERT INTO favorites (author_id, book_id) VALUES (4, 1);
INSERT INTO favorites (author_id, book_id) VALUES (4, 2);
INSERT INTO favorites (author_id, book_id) VALUES (4, 3);
INSERT INTO favorites (author_id, book_id) VALUES (4, 4);
INSERT INTO favorites (author_id, book_id) VALUES (4, 5);

SELECT author_id FROM favorites WHERE book_id = 3;

DELETE FROM favorites WHERE book_id = 3 LIMIT 1;

-- SELECT author_id FROM favorites WHERE book_id = 3 LIMIT 1; -- Selecting specificity using LIMIT in MYSQL

INSERT INTO favorites (author_id, book_id) VALUES (5, 2);

SELECT book_id FROM favorites WHERE author_id = 3;

SELECT author_id FROM favorites WHERE book_id = 5;


