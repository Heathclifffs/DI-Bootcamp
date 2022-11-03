-- Mise À Jour
-- 'Lea Benichou' et 'Marc Benichou' sont jumeaux, ils doivent avoir les mêmes dates de naissance. Mettez à jour leurs dates de naissance au 02/11/1998.
UPDATE eleve SET birth_date='02/11/1998' WHERE last_name='Benichou';
-- Changez le nom de famille de David de 'Grez' à 'Guez'.
UPDATE eleve SET last_name='Guez' WHERE last_name='Grez';
-- Effacer
-- Supprimez l'élève nommée 'Lea Benichou' du tableau.
DELETE FROM eleve WHERE first_name='Ici';
-- Compter
-- Comptez le nombre d'élèves dans le tableau.
SELECT COUNT(*) FROM eleve;
-- Comptez le nombre d'élèves né.s après le 1/01/2000.
SELECT COUNT(*) FROM eleve WHERE birth_date>'1/01/2000';
-- Insérer / Modifier
-- Ajoutez une colonne à la table des étudiants appelée math_grade .
ALTER TABLE etudiants  Add COLUMN math_grade  integer; 
ALTER TABLE etudiantS ALTER COLUMN  math_grade DROP  NOT NULL;
A REFAIRE

-- Ajoutez 80 à l'étudiant dont l'identifiant est 1.
INSERT INTO etudiants (math_grade) VALUES(80)  ;
ALTER TABLE etudiants DROP math_grade;
-- Ajoutez 90 aux étudiants qui ont des identifiants de 2 ou 4.
-- Ajoutez 40 à l'élève dont l'identifiant est 6.
-- Comptez combien d'élèves ont une note supérieure à 83
-- Ajoutez un autre étudiant nommé "Omer Simpson" avec la même date_de_naissance que celui déjà dans le tableau. Donnez-lui une note de 70.
-- Maintenant, dans le tableau, "Omer Simpson" devrait apparaître deux fois. C'est le même élève, bien qu'il ait reçu 2 notes différentes parce qu'il a repris l'examen de mathématiques.
-- Bonus : Comptez le nombre de notes de chaque élève.
-- Astuce : Vous devez afficher le prénom, le nom et le nombre de notes de chaque élève. Si vous avez suivi correctement les instructions ci-dessus, tous les élèves devraient avoir 1 note en mathématiques, sauf Omer Simpson qui en a 2.
-- Astuce : Utilisez un alias appelé total_grade pour récupérer les notes.
-- Astuce : Utilisez GROUP BY.
-- SOMME
-- Trouver la somme de toutes les notes des élèves.
