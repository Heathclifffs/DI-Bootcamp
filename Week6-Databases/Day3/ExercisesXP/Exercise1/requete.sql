--Exercice 1 : Location De DVD
-- Des Instructions
-- Obtenez une liste de toutes les langues du film.
SELECT film.title,language.name FROM film INNER JOIN language ON film.language_id=language.language_id;
-- Obtenez une liste de tous les films joints avec leurs langues - sélectionnez les détails suivants : titre du film, description et nom de la langue. Essayez votre requête avec différentes jointures :
SELECT film.title,film.description,language.name FROM film INNER JOIN language ON film.language_id=language.language_id;
-- Obtenez tous les films, même s'ils n'ont pas de langues.
SELECT film.title,film.description,language.name FROM film FULL OUTER JOIN language ON film.language_id=language.language_id;
-- Obtenez toutes les langues, même s'il n'y a pas de films dans ces langues.
SELECT name FROM language FULL OUTER  JOIN film ON language.language_id=film.language_id;
-- Créez une nouvelle table nommée new_film avec les colonnes suivantes : id, name. Ajoutez quelques nouveaux films à la table.
CREATE TABLE new_film(
	id_new_film SERIAL,
	PRIMARY KEY(id_new_film),
	name VARCHAR(30) NOT NULL
);
-- insertion des donnees
INSERT INTO new_film(name) VALUES('Cout detat'),('Karate kid'),('Homme du president');
-- Créez une nouvelle table appelée customer_review , qui contiendra les critiques de films que les clients feront.
-- Pensez à la contrainte DELETE : si un film est supprimé, sa critique devrait être automatiquement supprimée.
-- Il devrait avoir les colonnes suivantes :
-- review_id - une clé primaire, non nulle, auto-incrémentée.
-- film_id – fait référence à la table new_film. Le film qui fait l'objet d'une critique.
-- language_id – fait référence à la table des langues. Dans quelle langue est l'avis.
-- titre – le titre de la critique.
-- note – la note de l'avis (1-10).
-- review_text – le texte de la critique. Aucune limite de longueur.
-- last_update – date à laquelle l'avis a été mis à jour pour la dernière fois.
CREATE TABLE customer_review(
	review_id SERIAL NOT NULL,
	PRIMARY KEY(review_id),
	film_id INTEGER,
	CONSTRAINT fk_film
		FOREIGN KEY (film_id) 
		REFERENCES new_film(id_new_film) ON DELETE CASCADE,
	language_id INTEGER,
	CONSTRAINT fk_language
		FOREIGN KEY (language_id)
		REFERENCES language(language_id),
	titre TEXT,
	note INTEGER,
	review_text TEXT,
	last_update DATE
);
-- Ajoutez 2 critiques de films. Assurez-vous de les lier à des objets valides dans les autres tables.
INSERT INTO customer_review(film_id,language_id,titre,note,review_text,last_update)VALUES (1,1,'Cout detat',6,'Un film trop calme,donne trop a reflechir','04/02/2020');
INSERT INTO customer_review(film_id,language_id,titre,note,review_text,last_update)VALUES (2,1,'Karate kid',8,'Un film chic avec beaucoup daction','07/02/2021');
INSERT INTO customer_review(film_id,language_id,titre,note,review_text,last_update)VALUES (3,1,'Homme du president',8,'Un film de strategie','01/01/2022');
-- Supprimer un film qui a une critique de la table new_film , qu'advient-il de la table customer_review
DELETE FROM new_film WHERE id_new_film=1;
-- au niveau de la table customer_review la critique correspondant a ete suprimer