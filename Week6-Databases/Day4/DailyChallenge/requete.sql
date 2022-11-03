-- Instructions
-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
CREATE TABLE product_orders(
	product_order_id SERIAL NOT NULL PRIMARY KEY,
	owner VARCHAR(100) NOT NULL
);
INSERT INTO product_orders(owner)
VALUES ('Leon'),
		('Siffa'),
		('Alucar');
CREATE TABLE items(
	items_id SERIAL NOT NULL PRIMARY KEY,
	price INTEGER NOT NULL,
	product_order_id INTEGER,
	CONSTRAINT fk_order FOREIGN KEY (product_order_id)
	REFERENCES product_orders (product_order_id)
);

INSERT INTO items(price,product_order_id)
VALUES (10000,(select product_order_id from product_orders where owner ILIKE '%Leon%')),
		(7000,(select product_order_id from product_orders where owner ILIKE '%Alucar%')),
		(15000,(select product_order_id from product_orders where owner ILIKE '%Leon%'));
		
-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.
create or replace function total_price(order_id INTEGER)
returns INTEGER
language plpgsql
as
$$
declare
   counter integer;
begin
   return(select sum(price) 
   from items
	where order_id = items.product_order_id);
--    return counter;
end;
$$;

-- TEST
SELECT total_price(product_order_id) FROM items
WHERE product_order_id = (select product_order_id from product_orders where owner ILIKE '%Leon%' LIMIT 1);

-- Bonus :
-- Create a table called users.
CREATE TABLE users(
	user_id SERIAL NOT NULL PRIMARY KEY,
	profil VARCHAR(100) NOT NULL,
	product_order_id INTEGER,
	CONSTRAINT fk_prdct_order FOREIGN KEY (product_order_id)
	REFERENCES product_orders (product_order_id)
);

INSERT INTO users(profil,product_order_id)
VALUES ('Alex',(select product_order_id from product_orders where owner ILIKE '%Leon%')),
		('Ange',(select product_order_id from product_orders where owner ILIKE '%Alucar%'));
-- There should be a one to many relationship between the users table and the product_orders table.
-- Create a function that returns the total price for a given order of a given user.
create or replace function user_total_price(usr_id INTEGER,ord_id INTEGER)
returns INTEGER
language plpgsql
as
$$
declare
   counter integer;
begin
    return(select sum(i.price) 
    from items as i
	join product_orders as o on o.product_order_id = i.product_order_id
	join users as u on u.product_order_id = o.product_order_id
	where ord_id = i.product_order_id
	and usr_id = u.user_id);
--     return counter;
end;
$$;

-- Test

SELECT user_total_price(user_id,product_order_id) FROM users
WHERE product_order_id = (select product_order_id from product_orders where owner ILIKE '%Leon%')
AND user_id = (select user_id from users where profil ILIKE '%Alex%');

