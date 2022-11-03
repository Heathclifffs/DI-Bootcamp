-- Des Instructions
-- Vous allez pratiquer les relations entre les tables

-- Première partie

-- Créez 2 tables : Client et Profil client. Ils ont une relation One to One.

-- Un client ne peut avoir qu'un seul profil et un profil appartient à un seul client
-- La table Customer doit avoir les colonnes : id, first_name,last_name NOT NULL
-- La table de profil Client doit avoir les colonnes : id, isLoggedIn DEFAULT false(un booléen), customer_id(une référence à la table Client)
CREATE TABLE client(
	id SERIAL,
	PRIMARY KEY(id),
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL
);
CREATE TABLE profil_client(
	pk_id INTEGER NOT NULL,
	PRIMARY KEY(pk_id),
	isLoggedIn BOOLEAN,
	CONSTRAINT pk_id FOREIGN KEY (pk_id) REFERENCES client(id)
);
-- Insérez ces clients

-- Jean, biche
-- Jérôme, Alors
-- Léa, Rive
INSERT INTO client(first_name,last_name) VALUES('Jean','biche'),('Jerome','Alors'),('Lea','Rive');
-- Insérez ces profils clients, utilisez des sous-requêtes

-- Jean est connecté
-- Jérôme n'est pas connecté
INSERT INTO profil_client (pk_id,isLoggedIn) VALUES(1,TRUE);
INSERT INTO profil_client (pk_id,isLoggedIn) VALUES(2,FALSE);

-- Utilisez les types de jointures pertinents pour afficher :
-- Le prénom des clients connectés
SELECT client.first_name FROM client INNER JOIN profil_client ON client.id=profil_client.pk_id WHERE profil_client.isLoggedIn='TRUE';
-- Toutes les colonnes first_name et isLoggedIn des clients - même les clients qui n'ont pas de profil.
SELECT client.first_name FROM client FULL OUTER JOIN profil_client ON client.id=profil_client.pk_id;
-- Le nombre de clients non connectés
SELECT COUNT(client.first_name) FROM client INNER JOIN profil_client ON client.id=profil_client.pk_id WHERE profil_client.isLoggedIn='FALSE';
-- Partie II :
-- Créez une table nommée Book , avec les colonnes : book_id SERIAL PRIMARY KEY, title NOT NULL,author NOT NULL
CREATE TABLE Book(
	book_id SERIAL,
	PRIMARY KEY(book_id),
	title VARCHAR(30) NOT NULL,
	author VARCHAR(30) NOT NULL
);
-- Insérez ces livres :
-- Alice au pays des merveilles, Lewis Carroll
-- Harry Potter, JK Rowling
-- Pour tuer un oiseau moqueur, Harper Lee
INSERT INTO Book(title,author) VALUES('Alice au pays des merveilles','Lewis Carroll'),
('Harry Potter','JK Rowling'),(' Pour tuer un oiseau moqueur','Harper Lee');
-- Créez une table nommée Student , avec les colonnes : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Assurez-vous que l'âge n'est jamais supérieur à 15 ans (Recherchez une méthode SQL) ;
CREATE TABLE etudiants(
	etudiant_id SERIAL,
	PRIMARY KEY(etudiant_id),
	nom VARCHAR(30) NOT NULL UNIQUE,
	age INTEGER CHECK(age<15)
);
-- Insérez ces étudiants :
-- Jean, 12 ans
-- Couche, 11
-- Patrick, 10 ans
-- Bob, 14 ans
INSERT INTO etudiants(nom,age) VALUES('Jean', 12),('Couche', 11),('Patrick',10),('Bob',14);
-- Créez une table nommée Library , avec les colonnes :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- Cette table, est une table de jonction pour une relation Plusieurs à Plusieurs avec les tables Livre et Élève : Un élève peut emprunter plusieurs livres, et un livre peut être emprunté par plusieurs enfants
-- book_fk_idest une clé étrangère représentant la colonne book_idde la table Book
-- student_fk_idest une clé étrangère représentant la colonne student_idde la table Student
-- La paire de clés étrangères est la clé primaire de la table de jonction
CREATE TABLE librairie(
	book_fk_id INTEGER,
	CONSTRAINT book_fk_id 
		FOREIGN KEY (book_fk_id)
		REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	etudiant_id INTEGER,
	CONSTRAINT etudiant_id
		FOREIGN KEY (etudiant_id)
		REFERENCES etudiants(etudiant_id) ON DELETE CASCADE ON UPDATE CASCADE,
	borrowed_date DATE
);
-- Ajoutez 4 enregistrements dans la table de jonction, utilisez des sous-requêtes.
-- l'étudiant nommé Jean , a emprunté le livre Alice au pays des merveilles le 15/02/2022
	INSERT INTO librairie(book_fk_id,etudiant_id,borrowed_date) VALUES
	((SELECT etudiant_id FROM etudiants WHERE etudiant_id=1),
	(SELECT book_id FROM book WHERE book_id=1),'15-02-2022'));
-- l'étudiant nommé couche , a emprunté le livre To kill a mockingbird le 03/03/2021
	INSERT INTO librairie(book_fk_id,etudiant_id,borrowed_date) VALUES
	((SELECT etudiant_id FROM etudiants WHERE etudiant_id=2),
	(SELECT book_id FROM book WHERE book_id=2),'03-03-2021'));
-- l'étudiante nommée Patrick , a emprunté le livre Alice au pays des merveilles le 23/05/2021
INSERT INTO librairie(book_fk_id,etudiant_id,borrowed_date) VALUES
	((SELECT etudiant_id FROM etudiants WHERE etudiant_id=1),
		(SELECT book_id FROM book WHERE book_id=1),'23-05-2021');


-- l'étudiant nommé Bob , a emprunté le livre Harry Potter le 12/08/2021
INSERT INTO librairie(book_fk_id,etudiant_id,borrowed_date) VALUES
	((SELECT etudiant_id FROM etudiants WHERE etudiant_id=2),
	 	(SELECT book_id FROM book WHERE book_id=2),'12-08-2021');
-- Afficher les données
-- Sélectionnez toutes les colonnes de la table de jonction
SELECT * FROM librairie;
-- Sélectionnez le nom de l'élève et le titre des livres empruntés
SELECT etudiants.nom,book.title FROM etudiants INNER JOIN book ON etudiants.etudiant_id=book.book_id;
-- Sélectionnez l'âge moyen des enfants qui ont emprunté le livre Alice au pays des merveilles
SELECT AVG(age) FROM etudiants INNER JOIN book ON etudiants.etudiant_id=book.book_id WHERE book.title='Alice au pays des merveilles';
-- Supprimer un étudiant de la table des étudiants, que s'est-il passé dans la table de jonction ?
DELETE FROM etudiants WHERE etudiant_id=2;