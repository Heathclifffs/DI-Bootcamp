-- 🌟 Instruction De Sélection De Base
-- Écrivez une requête pour afficher les noms (prénom, nom) en utilisant un nom d'alias "Prénom", "Nom" de la table des employés.
SELECT first_name AS prenom,last_name AS nom FROM employees;
-- Écrivez une requête pour obtenir un ID de service unique à partir de la table des employés (c'est-à-dire sans doublons).
SELECT DISTINCT(employees.department_id) FROM employees INNER JOIN departments ON employees.department_id=departments.department_id;
-- Écrivez une requête pour obtenir les détails de tous les employés de la table des employés, faites-le par ordre décroissant de prénom.
SELECT * FROM employees ORDER BY first_name DESC;
-- Écrivez une requête pour obtenir les noms (prénom, nom), le salaire et 15 % du salaire en tant que PF (c'est-à-dire alias) pour tous les employés.
SELECT first_name,last_name,salary,(salary*15)/100 AS PF FROM employees ; 
-- Écrivez une requête pour obtenir les identifiants, les noms (prénom, nom) et le salaire des employés par ordre croissant en fonction de leur salaire.
SELECT first_name,last_name,salary FROM employees ORDER BY salary ASC;
-- Écrivez une requête pour obtenir la somme totale de tous les salaires versés aux employés.
SELECT SUM(salary) AS somme_totale_salaire FROM employees;
-- Rédigez une requête pour obtenir les salaires maximum et minimum versés aux employés.
SELECT MIN(salary) AS salaire_minimum,MAX(salary) AS salaire_maximun FROM employees;
-- Rédigez une requête pour obtenir le salaire moyen versé aux employés.
SELECT AVG(salary) AS salaire_moyen FROM employees;
-- Rédigez une requête pour obtenir le nombre d'employés travaillant dans l'entreprise.
SELECT COUNT(*) FROM employees;
-- Écrivez une requête pour obtenir tous les prénoms de la table des employés en majuscules.
SELECT UPPER(first_name) FROM employees;
-- Écrivez une requête pour obtenir les trois premiers caractères de chaque prénom de tous les employés de la table des employés.
SELECT LEFT(first_name,3) FROM employees;
-- Écrivez une requête pour obtenir les noms complets de tous les employés de la table des employés. Vous devez inclure le prénom et le nom de famille.
SELECT CONCAT(first_name,' ' ,last_name)AS full_name FROM employees;
-- Écrivez une requête pour obtenir le prénom, le nom et la longueur du nom complet de tous les employés de la table des employés.
SELECT first_name,last_name,LENGTH(last_name) AS longueur_prenom FROM employees; 
-- Écrivez une requête pour vérifier si la colonne first_name de la table des employés contient des nombres.
??
-- Écrivez une requête pour sélectionner les dix premiers enregistrements d'une table.
SELECT first_name,last_name FROM employees LIMIT 10;
-- 🌟 Restriction Et Tri
-- Rédigez une requête pour afficher le prénom, le nom et le salaire de tous les employés dont le salaire est compris entre 10 000 $ et 15 000 $.
SELECT first_name,last_name,salary FROM employees WHERE salary BETWEEN 10000 AND 15000; 
-- Rédigez une requête pour afficher le prénom, le nom et la date d'embauche de tous les employés qui ont été embauchés en 1987.
SELECT first_name,last_name,hire_date FROM employees WHERE hire_date='1987';
-- Écrivez une requête pour obtenir tous les employés dont le prénom contient à la fois les lettres « c » et « e ».
SELECT first_name FROM employees WHERE first_name LIKE '%e%' AND first_name LIKE '%c%';
-- Rédigez une requête pour afficher le nom, le poste et le salaire de tous les employés qui ne travaillent pas en tant que programmeurs ou commis à l'expédition et qui ne reçoivent pas un salaire égal à 4 500 $, 10 000 $ ou 15 000 $.
SELECT employees.last_name,employees.salary,jobs.job_title FROM employees INNER JOIN jobs ON jobs.job_id=employees.job_id WHERE jobs.job_title !='Programmer' AND
employees.salary=4500 OR employees.salary=10000 OR employees.salary=15000 ;
-- Écrivez une requête pour afficher les noms de famille de tous les employés dont le nom de famille contient exactement six caractères.
SELECT LEFT(last_name,6)FROM employees;
-- Écrivez une requête pour afficher le nom de famille de tous les employés qui ont la lettre « e » comme troisième caractère dans le nom.
SELECT last_name FROM employees WHERE last_name LIKE '_e_';
-- Écrivez une requête pour afficher le titre des emplois apparaissant dans la table des employés.
SELECT jobs.job_title FROM jobs INNER JOIN employees ON employees.job_id=jobs.job_id;
-- Écrivez une requête pour sélectionner toutes les informations des employés dont le nom de famille est 'JONES' ou 'BLAKE' ou 'SCOTT' ou 'KING' ou 'FORD'.
SELECT * FROM employees WHERE last_name='Jones' OR last_name='Blake' OR last_name='Scoot' OR last_name='King' OR last_name='Ford';
