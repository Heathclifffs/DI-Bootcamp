-- Mettre À Jour La Déclaration
-- Écrivez une instruction SQL pour modifier les détails suivants appartenant à tous les employés dont le department_id est 110 :
-- la colonne e-mail doit être : 'non disponible'
-- La colonne commission_pct doit être : 0,10
-- LE DEPARTEMENT 110 NE FIGURE PAS DANS LES TABLES NI LA COLONNE COMISSION_PTC
-- Écrivez une instruction SQL qui changera la colonne e-mail de tous les employés en 'disponible' qui travaillent dans le département 'Comptabilité'.
UPDATE employees SET email='disponible' FROM employees e INNER JOIN departments t ON e.department_id=t.department_id  WHERE t.department_name='Accounting'; 
-- Écrivez une instruction SQL pour modifier le salaire de l'employé dont l'ID est 105. Si le salaire existant est inférieur à 5 000, remplacez-le par 8 000.
UPDATE employees SET salary=8000 WHERE employee_id=105 AND salary<5000;



-- Fonctions D'agrégation
-- Écrivez une requête pour trouver le nombre d'emplois disponibles dans la table des employés.
SELECT COUNT(employee_id) FROM employees;
-- Rédigez une requête pour obtenir le nombre d'employés travaillant dans chaque poste.
SELECT COUNT(first_name),jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id GROUP BY jobs.job_title;
-- Rédigez une requête pour obtenir la différence entre les salaires les plus élevés et les plus bas.
SELECT MAX(salary)-MIN(salary) AS Difference_salaire  FROM employees;
-- Rédigez une requête pour trouver un identifiant de responsable et le salaire de l'employé le moins bien payé sous ce responsable.
?
-- Rédigez une requête pour obtenir le salaire moyen pour chaque poste hors programmeur.
SELECT AVG(salary),jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE jobs.job_title !='Programmer' GROUP BY jobs.job_title; 
-- Rédigez une requête pour obtenir le salaire moyen de tous les départements qui emploient plus de 10 employés.

SELECT AVG(salary),COUNT(employees.first_name) AS nombre_employe,departments.department_name FROM employees INNER JOIN departments ON employees.department_id=departments.department_id  GROUP BY(departments.department_name); 
?
-- Modifier L'instruction De Table
-- Écrivez une instruction SQL pour changer le nom de la colonne « state_province » en « state » dans la table des emplacements, en conservant le même type de données et la même taille.
ALTER TABLE locations RENAME COLUMN state_province TO state; 
-- Écrivez une instruction SQL pour ajouter une clé primaire à la colonne "location_id" dans la table des emplacements.
-- location_id est deja defini comm cle primaire
-- Créer Des Tableaux
-- Quelques avis :

-- L'action ON UPDATE CASCADE permet d'effectuer la mise à jour du tableau croisé
-- L'action ON DELETE RESTRICT rejette la suppression.
-- L'action ON DELETE CASCADE permet de supprimer des enregistrements dans la table des employés (enfant) qui fait référence à un enregistrement dans la table des emplois (parent) lorsque l'enregistrement dans la table parent est supprimé
-- L'action ON DELETE SET NULL définira les valeurs de la colonne de clé étrangère dans la table enfant (employés) sur NULL lorsque l'enregistrement dans la table parent (emplois) est supprimé, à condition que la colonne de clé étrangère dans la table enfant accepte les valeurs NULL .
-- L'action ON UPDATE SET NULL réinitialise les valeurs des lignes de la table enfant (employés) sur les valeurs NULL lorsque les lignes de la table parent (emplois) sont mises à jour.
-- L'action par défaut est ON DELETE RESTRICT .
-- ON DELETE NO ACTION et ON UPDATE NO ACTION rejetteront la suppression et toute mise à jour.


-- Vous devez décider quelle contrainte doit être utilisée dans chaque question ci-dessous :



-- Écrivez une instruction SQL pour créer une table simple "new_countries" comprenant les colonnes country_id et country_name.
-- assurez-vous qu'aucune donnée en double n'est ajoutée à la colonne country_id (quel type de données devez-vous utiliser pour la colonne country_id ?)
-- assurez-vous qu'aucun pays, à l'exception de l'Italie, de l'Inde et de la Chine, ne figure dans le tableau.
CREATE TABLE new_country(
	country_id SERIAL,
	PRIMARY KEY(country_id),
	country_name VARCHAR(30) CHECK(country_name='Italie' OR country_name='Inde'
								  OR country_name='Chine')
);
-- Écrivez une instruction SQL pour créer une copie dupliquée de la table « new_countries » incluant la structure et les données de la table « new_countries ».
?
-- Écrivez une instruction SQL pour créer une table nommée "new_jobs" comprenant les colonnes job_id, job_title, min_salary, max_salary
-- assurez-vous que la colonne max_salary ne dépasse pas 25 000.
-- assurez-vous que job_title, min_salary et max_salary ont les valeurs par défaut suivantes :
-- job_title est vide
-- min_salary est 8000
-- max_salary est NULL.
CREATE TABLE new_jobs(
	job_id INTEGER ,
	PRIMARY KEY(job_id),
	job_title VARCHAR(30) DEFAULT NULL,
	min_salary INTEGER DEFAULT 8000,
	max_salary INTEGER DEFAULT NULL CHECK(max_salary<=25000)
);
-- Écrivez une instruction SQL pour créer une table appelée "new_employees". La table doit inclure les colonnes suivantes : employee_id, first_name, last_name, email, phone_number embauche_date, job_id et salaire.
-- assurez-vous que la colonne employee_id ne contient aucune valeur en double au moment de l'insertion,
-- assurez-vous que la colonne de clé étrangère job_id fait référence à la colonne job_id dans la table "new_jobs".
CREATE TABLE new_employees(
	employee_id SERIAL ,
	PRIMARY KEY(employee_id),
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(30),
	phone_number VARCHAR(40),
	embauche_date DATE,
	job_id INTEGER,
	CONSTRAINT fk_job_id
		FOREIGN KEY (job_id) REFERENCES new_jobs(job_id) ON DELETE SET NULL
);
-- Écrivez une instruction SQL pour créer une table appelée "new_job_history" la table doit inclure les colonnes suivantes : employee_id, start_date, end_date, job_id
-- assurez-vous que la clé étrangère employee_id fait référence à la colonne employee_id dans la table « new_employees ».
-- assurez-vous que la clé étrangère job_id est égale à un identifiant qui existe dans la table "new_jobs".
CREATE TABLE new_job_history(
	employee_id INTEGER,
	CONSTRAINT fk_employee_id
		FOREIGN KEY (employee_id) REFERENCES new_employees(employee_id)	ON DELETE CASCADE ON UPDATE CASCADE	,
	start_date DATE,
	end_date DATE,
	job_id INTEGER,
	CONSTRAINT fk_job_id
		FOREIGN key(job_id) REFERENCES new_jobs(job_id) ON DELETE SET NULL ON UPDATE SET NULL
);

-- Insérer
-- Écrivez une instruction SQL pour insérer un enregistrement avec votre propre valeur dans la table « new_countries ».
INSERT INTO new_country(country_name) VALUES('Brazil');
-- donne une erreur a cause de la methode de verification CHECK
-- ?
-- En utilisant une seule instruction d'insertion, insérez 3 lignes de données dans la table "new_countries"
INSERT INTO new_country(country_name) VALUES('Italie'),('Inde'),('Chine');

-- Écrivez une instruction SQL pour insérer les lignes de la table "new_countries" dans une table dupliquée.

-- Écrivez une instruction SQL pour insérer des données dans la table "new_employees", la colonne job_id doit contenir des valeurs qui existent dans la table "new_jobs".
INSERT INTO new_jobs(job_id,job_title,min_salary,max_salary) VALUES(1,'Programmer',8000,0);
INSERT INTO new_employees(first_name,last_name,email,phone_number,embauche_date,job_id) VALUES('Jean','Pierre','piere@gmail.com','66.47.12.42','15/02/2020',1);

