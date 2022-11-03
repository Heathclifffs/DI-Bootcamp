-- Exercice 2 – Joyeux Halloween
-- Des Instructions
-- Il y a un fléau de zombies qui approche ! La société de location de DVD propose de prêter tous ses DVD aux refuges locaux, afin que les citoyens puissent regarder les films ensemble dans les refuges jusqu'à ce que les zombies soient détruits par les forces armées. Préparez des tableaux avec les données suivantes :
-- Combien y a-t-il de magasins, et dans quelle ville et dans quel pays ils se trouvent.
SELECT  COUNT(store.store_id),country.country,city.city FROM store  JOIN country ON country.country_id=store.store_id JOIN city ON country.country_id=city.country_id GROUP BY country.country, city.city;
-- Combien d'heures de temps de visionnage il y a au total dans chaque magasin - en d'autres termes, la somme de la durée de chaque article d'inventaire dans chaque magasin.
?
-- Assurez-vous d'exclure tous les articles en stock qui ne sont pas encore retournés. (Oui, même au temps des zombies il y a des gens qui ne rendent pas leurs DVD)
?
-- Une liste de tous les clients dans les villes où se trouvent les magasins.
SELECT customer.first_name FROM customer INNER JOIN store ON store.store_id=customer.store_id;
-- Une liste de tous les clients dans les pays où les magasins sont situés.
SELECT customer.first_name FROM customer INNER JOIN store ON store.store_id=customer.customer_id JOIN country ON store.store_id=country.country_id;
-- Certaines personnes seront effrayées en regardant des films effrayants pendant que des zombies marchent dans les rues. Créez une « liste sécurisée » de tous les films qui n'incluent pas la catégorie « Horreur » ou qui contiennent les mots « bête », « monstre », « fantôme », « mort », « zombie » ou « mort-vivant » dans leurs titres. ou des descriptions… Obtenez la somme de leur temps de visionnage (durée).
-- Astuce : utilisez la contrainte CHECK
?
-- Pour les listes « générales » et « sûres » ci-dessus, calculez également le temps en heures et en jours (pas seulement en minutes).
?