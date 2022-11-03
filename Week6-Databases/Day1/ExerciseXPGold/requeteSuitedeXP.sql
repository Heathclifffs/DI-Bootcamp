-- creation de la table etudiants
CREATE TABLE eleve(
	identifiant SERIAL NOT NULL,
	first_name VARCHAR(30) NOT NULL,	
	last_name VARCHAR(30) NOT NULL,
	birth_date DATE NOT NULL
);
-- insertion des donnees
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('Marc','Benichou','02/11/1998');
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('Yoan','Cohen','03/12/2010');
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('Ici','Benichou','27/07/1987');
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('Amelie','Chef','07/04/1996');
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('David','Grez','14/06/2003');
INSERT INTO eleve(first_name,last_name,birth_date) VALUES('Omer','Simpson','03/10/1980');
-- Pour les questions suivantes, récupérez uniquement les prénoms et noms de famille des élèves.
-- Récupérer l'étudiant dont l'id est égal à 2.
SELECT first_name ,last_name FROM eleve WHERE identifiant=2;
-- Récupérez l'élève dont le nom est Benichou ET le prénom est Marc.
SELECT first_name,last_name FROM eleve WHERE first_name='Marc' AND last_name='Benichou';
-- Récupérez les étudiants dont le nom de famille est Benichou OU dont le prénom est Marc
SELECT first_name,last_name FROM eleve WHERE first_name='Marc' OR last_name='Benichou';
-- Récupérez les étudiants dont les prénoms contiennent la lettre a .
SELECT first_name FROM eleve WHERE firsT_name LIKE '%a%';
-- Récupérez les étudiants dont le prénom commence par la lettre a .
SELECT first_name FROM eleve WHERE first_name LIKE 'a%';
-- Récupérer les étudiants dont les prénoms se terminent par la lettre a .
SELECT first_name FROM eleve WHERE first_name LIKE '%a';
-- Récupérer les étudiants dont les identifiants sont égaux à 1 AND 3 .
SELECT first_name,last_name FROM eleve WHERE identifiant=1 AND identifiant=2 ;
-- Récupérez les étudiants dont la date de naissance est égale ou postérieure au 01/01/2000. (afficher toutes leurs informations).
SELECT first_name,last_name,birth_date FROM eleve WHERE birth_date>='01/01/2000';
-- SUITE DE LEXO XP
-- Va chercher les quatre premiers étudiants. Vous devez classer les quatre étudiants par ordre alphabétique de nom_de_famille.
SELECT first_name,last_name FROM eleve  ORDER BY  last_name ASC;
-- Récupérez les coordonnées du plus jeune étudiant.
SELECT first_name,last_name,birth_date FROM eleve WHERE birth_date='2010=12-03'
-- Allez chercher trois élèves en sautant les deux premiers élèves.
SELECT first_name,last_name,birth_date FROM eleve OFFSET 2;