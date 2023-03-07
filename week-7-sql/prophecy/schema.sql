.schema

SELECT * FROM students;

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE assignments (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(id),
    PRIMARY KEY(student_id, house_id)
);

.schema

SELECT * FROM houses;
SELECT * FROM students;
SELECT * FROM assignments;

SELECT COUNT(student_id) FROM assignments WHERE house_id = ( SELECT id FROM houses WHERE house = 'Gryffindor');

SELECT * FROM assignments JOIN houses ON houses.id = assignments.house_id;

SELECT house, COUNT(student_id) FROM assignments JOIN houses ON houses.id = assignments.house_id GROUP BY house;

SELECt * FROM students
JOIN assignments ON students.id = assignments.student_id
JOIN houses ON houses.id = assignments.house_id;


-- Create a temporary table without the temp_id and id columns
CREATE TABLE temp_assignments AS
SELECT student_id, house_id
FROM assignments;

-- Drop the original assignments table
DROP TABLE assignments;

-- Rename the temporary table to assignments
ALTER TABLE temp_assignments RENAME TO assignments;




-- Create a temporary table without the house and head columns
CREATE TABLE temp_students AS
SELECT id, student_name
FROM students;

-- Drop the original assignments table
DROP TABLE students;

-- Rename the temporary table to assignments
ALTER TABLE temp_students RENAME TO students;
