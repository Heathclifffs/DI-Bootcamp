-- Exercice 2 : Location De DVD
-- Des Instructions
-- Utilisez UPDATE pour changer la langue de certains films. Assurez-vous d'utiliser des langues valides.
UPDATE language SET name='French' WHERE language_id=1
-- Quelles clés étrangères (références) sont définies pour la table client ? Comment cela affecte-t-il la manière dont nous INSÉRONS dans la table client ?
-- les cles etrangeres store_id,address_id,
A FEFAIRE
-- Nous avons créé une nouvelle table appelée customer_review . Déposez ce tableau. Est-ce une étape facile ou nécessite-t-elle une vérification supplémentaire ?
SELECT * FROM customer_review;
DROP TABLE customer_review;
-- Découvrez combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).
SELECT COUNT(*) FROM rental;
-- Trouvez les 30 films les plus chers qui sont exceptionnels (c'est-à-dire qui n'ont pas encore été retournés au magasin)
SELECT film.title FROM film INNER JOIN rental ON rental.customer_id=film.film_id LIMIT 30;
-- Votre ami est au magasin et décide de louer un film. Il sait qu'il veut voir 4 films, mais il ne se souvient pas de leurs noms. Pouvez-vous l'aider à trouver les films qu'il souhaite louer ?
-- Le 1er film : Le film parle d'un lutteur de sumo, et l'un des acteurs est Penelope Monroe.
SELECT film.title,actor.first_name,actor.last_name FROM film INNER JOIN actor ON film.film_id=actor.actor_id WHERE actor.first_name='Penelope' AND actor.last_name='Monroe' AND film.description='A Sumo wrestlers';
-- Le 2ème film : Un court documentaire (moins d'1h), noté « R ».
A refaire
-- Le 3ème film : Un film que son ami Matthew Mahan a loué. Il a payé plus de 4,00 $ pour la location et il l'a rendue entre le 28 juillet et le 1er août 2005.
SELECT film.title,customer.first_name,customer.last_name FROM film INNER JOIN customer ON film.film_id=customer.customer_id WHERE first_name='Matthew' AND last_name='Mahan' AND film.rental_rate>4.00;
-- Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il y avait le mot «bateau» dans le titre ou la description, et il semblait que c'était un DVD très coûteux à remplacer.
SELECT film.title,film.description,customer.first_name,customer.last_name FROM film INNER JOIN customer ON film.film_id=customer.customer_id WHERE first_name='Matthew' AND last_name='Mahan' AND film.rental_rate>4.00
AND film.title LIKE 'Beat' OR film.description LIKE '_beat_';
