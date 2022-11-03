-- Découvrez combien de films il y a pour chaque classement.
SELECT rating,COUNT(rating) FROM film GROUP BY rating;
-- Obtenez une liste de tous les films classés G ou PG-13.
SELECT title FROM film WHERE rating='G' OR rating='PG-13';
-- Filtrez davantage cette liste : recherchez uniquement les films qui durent moins de 2 heures et dont le prix de location (rental_rate) est inférieur à 3,00. Triez la liste par ordre alphabétique
SELECT title FROM film WHERE rental_duration<2 AND rental_rate<3.00   ORDER BY title ASC;
-- Recherchez un client dans la table des clients et remplacez ses coordonnées par vos coordonnées à l'aide de SQL UPDATE.
UPDATE customer SET first_name='yel',last_name='some',email='yel@gmail.com' WHERE customer_id=524;
-- Trouvez maintenant l'adresse du client et utilisez UPDATE pour remplacer l'adresse par votre adresse (ou créez-en une).
SELECT address,first_name FROM address INNER JOIN customer ON address.address_id=customer.address_id;
UPDATE address SET address='Burkina-Faso' WHERE address='1913 Hanoi Way';