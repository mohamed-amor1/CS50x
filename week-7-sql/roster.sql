-- SQLite
SELECT student_name, house
FROM students
WHERE student_name LIKE "%Potter";

-- Student names that start with H or h
SELECT student_name, house
FROM students
WHERE student_name LIKE "H%";

SELECT student_name, house
FROM students
WHERE house = 'Hufflepuff';

-- data is case sensitive
SELECT student_name
FROM students
WHERE student_name = "Harry James Potter";

-- this won't work
SELECT student_name
FROM students
WHERE student_name = "harry james potter";

-- Ordering. ASC is by default
SELECT *
FROM students
ORDER BY student_name;

-- Ordering DESC 
SELECT *
FROM students
ORDER BY student_name DESC;

-- 
SELECT *
FROM students
ORDER BY house;

-- Sort first by house and then by student name
SELECT *
FROM students
ORDER BY house, student_name;

--
SELECT * FROM students
ORDER BY house, student_name DESC;

-- SQL column names are not case sensitive
SELECT *
FROM students
ORDER BY House, student_name;

--
SELECT * FROM students
ORDER BY student_name, house;

-- sort one column ASC and other DESC
SELECT * FROM students
ORDER BY house DESC, student_name ASC;

-- LIMIT
SELECT * FROM students
ORDER BY student_name
LIMIT 10;

-- LIMIT
SELECT * FROM students
ORDER BY student_name DESC
LIMIT 10;

-- Aggregating
SELECT COUNT(*)
FROM students;

-- Change column name to show
SELECT COUNT(*) AS number_of_students
FROM students;

-- Aggregating
SELECT COUNT(*)
FROM students
WHERE house = 'Gryffindor';

-- Aggregating
SELECT COUNT(*)
FROM students
WHERE house = 'Slytherin';

-- GROUP BY house then counting
SELECT house, COUNT(*)
FROM students
GROUP BY house;

-- Database Design
-- Each table should be a collection of a single entity
-- For example, we should have a different table for each of students, houses, and student-house assignments

/* Each piece of data should be stored in a single location
and thereafter referred to by its ID ("primary key") 
For example, we should ensure every student and house has an ID, then use thoses IDSs in the 
house assignments table.
*/

-- Creating new tables
CREATE TABLE houses (
id INTEGER NOT NULL,
house TEXT NOT NULL,
head TEXT NOT NULL,
PRIMARY KEY(id)
);

-- NOT NULL : "required"

.schema

SELECT * FROM houses;

-- Inserting
INSERT INTO houses(house, head)
VALUES ('Gryffindor', 'McGonagall');
SELECT * FROM houses;

INSERT INTO houses (house, head)
VALUES ('Slytherin', 'Severus Snape');
SELECT * FROM houses;

-- SELECTs (nesting)
SELECT COUNT(student_id)
FROM assignments
WHERE house_id = 
(
    SELECT id
    FROM houses
    WHERE house = 'Gryffindor'
);

-- JOIN (combining tables together)
SELECT * FROM assignments
JOIN houses
ON assignments.house_id = houses.id;