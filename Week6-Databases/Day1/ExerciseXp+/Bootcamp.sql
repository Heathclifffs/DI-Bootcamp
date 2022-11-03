-- 🌟 Exercise 1 : Bootcamp
-- Instructions
-- For this exercise, you will have to find some requests on your own!



-- Create
-- Create a database called bootcamp.
-- Create a table called students.
-- Add the following columns:
-- id
-- last_name
-- first_name
-- birth_date
-- The id must be auto_incremented.
-- Make sure to choose the correct data type for each column.
-- To help, here is the data that you will have to insert. (How do we insert a date to a table?)


-- Here is the data:

-- id	first_name	last_name	birth_date
-- 1	Marc	Benichou	02/11/1998
-- 2	Yoan	Cohen	03/12/2010
-- 3	Lea	Benichou	27/07/1987
-- 4	Amelia	Dux	07/04/1996
-- 5	David	Grez	14/06/2003
-- 6	Omer	Simpson	03/10/1980


-- Insert
-- Insert the data seen above to the students table. Find the most efficient way to insert the data.
-- Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).


-- Select
-- Fetch all of the data from the table.
-- Fetch all of the students first_names and last_names.
-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.
-- Fetch the student whose last_name is Benichou AND first_name is Marc.
-- Fetch the students whose last_names are Benichou OR first_names are Marc.
-- Fetch the students whose first_names contain the letter a.
-- Fetch the students whose first_names start with the letter a.
-- Fetch the students whose first_names end with the letter a.
-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
-- Fetch the students whose id’s are equal to 1 AND 3 .

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
--------------------------------------
--------------------------------------
-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_Burkina Faso.1252'
--     LC_CTYPE = 'French_Burkina Faso.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

CREATE TABLE student(
	student_id SERIAL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	birth_date DATE NOT NULL
);

INSERT INTO student(first_name,last_name,birth_date)
VALUES	
	('Marc',	'Benichou',	'02/11/1998'),
	('Yoan'	,'Cohen'	,'03/12/2010'),
	('Lea'	,'Benichou'	,'27/07/1987'),
	('Amelia',	'Dux',	'07/04/1996'),
	('David',	'Grez',	'14/06/2003'),
	('Omer',	'Simpson',	'03/10/1980');

INSERT INTO student(first_name,last_name,birth_date)
VALUES	
	('Abdoul',	'Gafar',	'08/12/1999')
RETURNING student_id;

select * from student;
SELECT last_name,first_name FROM student;
SELECT * FROM student WHERE last_name = 'Benichou' OR first_name ='Marc'
SELECT * FROM student WHERE first_name LIKE '%a%';
SELECT * FROM student WHERE first_name  ILIKE 'a%';
SELECT * FROM student WHERE first_name  ILIKE '%a';
SELECT * FROM student WHERE first_name  ILIKE '%a_';
SELECT * FROM student WHERE student_id = 1  OR student_id = 3;
SELECT * FROM student WHERE birth_date >= '1/01/2000';



