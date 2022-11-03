-- Première partie

-- Créez une table nommée achats . Il doit avoir 3 colonnes :
-- id: la clé primaire de la table
-- customer_id: cette colonne référence la table clients
-- item_id: cette colonne référence les éléments du tableau
-- quantity_purchased: cette colonne est la quantité d'articles achetés par un certain client
CREATE TABLE achats(
	id SERIAL,
	customer_id INTEGER,
	item_id INTEGER,
	quantity_purchased INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY(customer_id) REFERENCES  customers(id_customers),
	FOREIGN KEY(item_id) REFERENCES items(id_items)
);

-- Insérez les achats pour les clients, utilisez des sous-requêtes :
-- Scott Scott a acheté un ventilateur
INSERT INTO achats(customer_id,item_id,quantity_purchased) VALUES(3,3,1);
-- Melanie Johnson a acheté dix grands bureaux
INSERT INTO achats(customer_id,item_id,quantity_purchased) VALUES(5,2,10);
-- Greg Jones a acheté deux petits bureaux
INSERT INTO achats(customer_id,item_id,quantity_purchased) VALUES(1,1,2);
-- Partie II

-- Utilisez SQL pour obtenir les éléments suivants à partir de la base de données :
-- Tous les achats. Ces informations nous sont-elles utiles ?
SELECT * FROM achats;
-- Tous les achats, joint à la table des clients .
SELECT * FROM achats INNER JOIN customers ON achats.customer_id=customers.id_customers;
-- Achats du client avec l'ID égal à 5.
SELECT * FROM achats INNER JOIN customers ON achats.customer_id=customers.id_customers WHERE customers.id_customers=5;
-- Achats pour un grand bureau ET un petit bureau
SELECT * FROM achats INNER JOIN items ON achats.item_id=items.id_items WHERE items.nom='Grand bureau' OR items.nom='Petit bureau';
-- Utilisez SQL pour afficher tous les clients qui ont effectué un achat. Afficher les champs/colonnes suivants :
-- Prénom du client
-- Nom de famille du client
-- Nom de l'article
SELECT first_namets INNER JOIN customers ON achats.customer_id=customers.id_customers;
SELECT first_name,last_name,nom FROM customers INNER JOIN items ON items.id_items=customers.id_customers;
-- Ajoutez une ligne qui référence un client par ID, mais ne référence pas un article par ID (laissez-la vide). Est-ce que ça marche? Pourquoi pourquoi pas?
INSERT INTO achats(customer_id,item_id,quantity_purchased) VALUES(2,0,7);
-- ca ne marche pas,parceque la valeur 0 nest pas dans la table achats une valeur nas pas de reference
-- dans la table items

