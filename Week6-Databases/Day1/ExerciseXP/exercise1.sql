
-- 🌟 Exercise 1 : Items And Customers
-- Create a database called public.
-- Add two tables:
-- items
-- customers.


-- Follow the instructions below to determine which columns and data types to add to the two tables:

-- Add the following items to the items table:
-- 1 - Small Desk – 100 (ie. price)
-- 2 - Large desk – 300
-- 3 - Fan – 80

-- Add 5 new customers to the customers table:
-- 1 - Greg - Jones
-- 2 - Sandra - Jones
-- 3 - Scott - Scott
-- 4 - Trevor - Green
-- 5 - Melanie - Johnson

-- Use SQL to fetch the following data from the database:
-- All the items.
-- All the items with a price above 80 (80 not included).
-- All the items with a price below 300. (300 included)
-- All customers whose last name is ‘Smith’ (What will be your outcome?).
-- All customers whose last name is ‘Jones’.
-- All customers whose firstname is not ‘Scott’.
---------------------
---------------------


-- Database: public

-- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'French_Burkina Faso.1252'
--     LC_CTYPE = 'French_Burkina Faso.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;
	
CREATE TABLE IF NOT EXISTS items(
	item_id SERIAL,
	item VARCHAR(255) NOT NULL,
	price INT NOT NULL
);

CREATE TABLE IF NOT EXISTS customers(
	customer_id SERIAL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL
);

INSERT INTO items(item,price)
VALUES
	('Small Desk',100),
	('Large desk',300),
	('Fan',80);

INSERT INTO customers(first_name,last_name)
VALUES
	('Greg','Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Green'),
	('Melanie','Johnson');
	
select * from items;	
select * from items where price > 80;	
select * from items where price <= 300;

select * from customers where last_name = 'Smith';
select * from customers where last_name = 'Jones';
select * from customers where NOT first_name = 'Scott';


	
	
