-- Exercice 1 : Location De DVD
-- Des Instructions
-- Nous voulons encourager les familles et les enfants à profiter de nos films.
-- Récupérez tous les films classés G ou PG, qui ne sont pas actuellement loués (ils ont été rendus/n'ont jamais été empruntés).
SELECT title FROM film WHERE rating='G' OR rating='PG' AND rental_duration=0;
-- Créez une nouvelle table qui représentera une liste d'attente pour les films pour enfants. Cela permettra à un enfant d'ajouter son nom à la liste jusqu'à ce que le DVD soit disponible (a été retourné). Une fois que l'enfant prend le DVD, son nom doit être retiré de la liste d'attente (idéalement en utilisant des déclencheurs, mais nous ne les connaissons pas encore. Supposons que notre programme Python gère cela). Quelles références de table doivent être incluses ?
CREATE TABLE film_enfant(
	id_film_enfant SERIAL,
	PRIMARY KEY(id_film_enfant),
	nom_enfant VARCHAR(30) NOT NULL,
	nom_film VARCHAR(30) NOT NULL,
	film_id INTEGER,
	CONSTRAINT fk_film_id	
		FOREIGN KEY (film_id)
		REFERENCES film(film_id) ON DELETE CASCADE
);
-- Récupérez le nombre de personnes qui attendent le DVD de chaque enfant. Testez cela en ajoutant des lignes au tableau que vous avez créé à la question 2 ci-dessus.
?