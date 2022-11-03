CREATE TABLE actors(
	 actor_id SERIAL PRIMARY KEY,
	 first_name VARCHAR (50) NOT NULL,
	 last_name VARCHAR (100) NOT NULL,
	 age DATE NOT NULL,
	 number_oscars SMALLINT NOT NULL
);
-- selectionner tous les acteurs
SELECT * FROM actors;
-- insertion des donnees
INSERT INTO actors (first_name, last_name, age, numbers_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, numbers_oscars)
VALUES('George','Clooney','06/05/1961', 2);
-- selection des donnees
-- 	lacteur dont le prenom est Matt
SELECT * FROM actors WHERE first_name = 'Matt';
-- l'acteur dont le nombres d'oscars est superieure a 3
SELECT * FROM actors WHERE number_oscars >= 3;
-- l'acteur dont le prenom n;est pas Matt
SELECT last_name FROM actors WHERE first_name != 'Matt' ;
-- EXO
-- 1. Comptez le nombre d'acteurs dans le tableau.
SELECT COUNT(*) FROM actors;
-- Essayez d'ajouter un nouvel acteur avec des champs vides. Que pensez-vous que le résultat sera?
INSERT INTO actors(first_name,last_name,age,numbers_oscars) VALUES();
