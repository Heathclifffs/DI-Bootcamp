-- Récupérez les 2 derniers clients par ordre alphabétique (AZ) - excluez 'id' des résultats.
SELECT first_name,last_name FROM customers ORDER BY last_name ASC OFFSET 4
-- Utilisez SQL pour supprimer tous les achats effectués par Scott.
SELECT  * FROM achats INNER JOIN customers ON achats.customer_id=customers.id_customers WHERE last_name='Scott';
DELETE  FROM achats WHERE customer_id=3;
-- Scott existe-t-il toujours dans la table des clients, même s'il a été supprimé ? Essayez de le trouver.
SELECT  * FROM customers WHERE last_name='Scott';
-- Utilisez SQL pour trouver tous les achats. Joignez les achats à la table des clients , de sorte que la commande de Scott apparaisse, bien qu'au lieu du prénom et du nom du client, vous ne devriez voir que vide/vide. (Quel type de jointure devez-vous utiliser ?).
SELECT * FROM achats  RIGHT JOIN customers ON achats.customer_id=customers.id_customers;
-- Utilisez SQL pour trouver tous les achats. Joignez les achats à la table des clients , afin que la commande de Scott n'apparaisse PAS. (Quel type de jointure devez-vous utiliser ?)
SELECT * FROM achats  INNER JOIN customers ON achats.customer_id=customers.id_customers;
