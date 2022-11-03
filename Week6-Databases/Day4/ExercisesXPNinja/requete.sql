-- Jointures
-- Sous-requêtes
-- Fonction de chaîne


-- Sous-Requêtes
-- Écrivez une requête pour trouver le prénom, le nom et les salaires des employés qui ont un salaire plus élevé que l'employé dont le nom est Bull.
SELECT first_name,last_name,salary FROM employees WHERE salary>(SELECT salary FROM employees WHERE first_name='Lex');
-- Écrivez une sous-requête SQL pour trouver le prénom et le nom des employés sous un responsable qui travaille pour un service basé aux États-Unis.
?
--Conseil : écrivez des sous-requêtes à une seule ligne et à plusieurs lignes

-- Écrivez une sous-requête SQL pour trouver le prénom et le nom des employés qui travaillent en tant que managers.
SELECT employees.first_name,employees.last_name,jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE jobs.job_title LIKE '%Manager' 
-- Écrivez une sous-requête SQL pour trouver le(s) prénom(s) et nom(s) du ou des employés, dont le salaire est supérieur au salaire moyen des employés.
SELECT employees.first_name,employees.last_name,AVG(salary)  FROM employees GROUP BY (employees.first_name,employees.last_name);
?
-- Écrivez une sous-requête SQL pour trouver le(s) prénom(s) et nom(s) du ou des employés, dont le salaire est égal au salaire minimum de leur poste.
SELECT employees.first_name,employees.last_name,MIN(jobs.min_salary) FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE employees.salary=jobs.min_salary GROUP BY(employees.first_name,employees.last_name);
-- Rédigez une requête pour trouver les noms (prénom, nom) des employés qui ne sont pas des superviseurs.
SELECT employees.first_name,employees.last_name,jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE jobs.job_title!='_%Manager';
-- Écrivez une sous-requête SQL pour trouver l'identifiant, le prénom, le nom et le salaire de tous les employés dont le salaire est supérieur au salaire moyen de leur service.
SELECT employees.first_name,employees.last_name,jobs.job_title  FROM employees INNER JOIN jobs ON employees.job_id=Jobs.job_id WHERE employees.salary>(jobs.min_salary+jobs.max_salary)/2 GROUP BY (employees.first_name,employees.last_name,jobs.job_title,employees.salary);
-- Écrivez une sous-requête pour trouver le 5ème salaire maximum de tous les salaires.
SELECT salary FROM employees ORDER BY salary DESC OFFSET 4 LIMIT 1;
-- Écrivez une sous-requête pour trouver le 4ème salaire minimum de tous les salaires.
SELECT salary FROM employees ORDER BY salary ASC  OFFSET 3 LIMIT 1;
-- Écrivez une requête pour répertorier le nom et le numéro du service, de tous les services dans lesquels il n'y a pas d'employés.
SELECT employees.job_id,jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE employees.job_id=NULL;
-- Jointures
-- Écrivez une requête pour trouver les adresses (location_id, street_address, city, state_province, country_name) de tous les départements.
SELECT departments.department_name,countries.country_name,locations.country_id,locations.location_id,locations.street_address,locations.city,locations.state FROM departments INNER JOIN locations ON departments.location_id=locations.location_id JOIN countries ON locations.country_id=countries.country_id;
-- Écrivez une requête pour faire une jointure avec la table des employés et des services pour trouver le nom de l'employé, y compris le prénom et le nom, l'ID du service et le nom des services.
SELECT employees.first_name,employees.last_name,departments.department_id,departments.department_name FROM employees INNER JOIN departments ON employees.department_id=departments.department_id;
-- Écrivez une requête SQL pour faire une jointure avec trois tables : employés, départements et emplacements pour trouver le nom, y compris le prénom et le nom, les emplois, le nom du département et l'ID, des employés travaillant à Londres.
SELECT employees.first_name,employees.last_name,departments.department_id,departments.department_name FROM employees INNER JOIN departments ON employees.department_id=departments.department_id JOIN locations ON locations.location_id=departments.location_id WHERE locations.city='London';
-- Écrivez une requête pour faire une jointure avec deux tables pour trouver l'identifiant de l'employé, last_name en tant qu'Employé avec son manager_id et son nom en tant que Manager.
SELECT employees.employee_id,employees.last_name AS Employee,employees.manager_id,jobs.job_title FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id WHERE jobs.job_title LIKE '%Manager';
-- Écrivez une requête pour faire une jointure avec deux tables employés et départements, pour obtenir les employés travaillant dans chaque département (récupérez les détails des employés, ainsi que le nom et le numéro du département).
SELECT employees.first_name,employees.last_name,employees,employees.email ,departments.department_name,departments.department_id FROM employees INNER JOIN departments ON employees.department_id=departments.department_id GROUP BY(employees.first_name,employees.last_name,employees,employees.email,employees.* ,departments.department_id,departments.department_name);
-- Écrivez une requête pour faire une jointure afin de trouver les employés qui ont travaillé dans un service dont l'ID est 90 (récupérez l'ID de l'employé, le titre du poste et le nombre de jours où l'employé a travaillé).
SELECT employees.first_name,employees.employee_id ,departments.department_name,departments.department_id FROM employees INNER JOIN departments ON employees.department_id=departments.department_id WHERE departments.department_id=90);
-- pas id 90 dans la table department
-- Rédigez une requête pour créer une jointure avec trois tables, départements, employés et emplacements pour afficher le nom du département, le nom du responsable et la ville.
-- ?
-- Écrivez une requête pour faire une jointure avec deux tables, employés et emplois pour afficher l'intitulé du poste et le salaire moyen des employés.
SELECT jobs.job_title,AVG(employees.salary) FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id GROUP BY (jobs.job_title);
-- Écrivez une requête pour faire une jointure avec deux tables, employés et départements pour afficher le nom du département, le prénom et le nom, la date d'embauche et le salaire pour tous les managers qui ont acquis une expérience professionnelle de plus de 15 ans.
SELECT employees.first_name,employees.last_name,employees.hire_date,employees.salary,departments.department_name INNER JOIN departments ON employees.department_id=departments.department_id WHERE employe?
-- Fonction De Chaîne
-- Rédigez une requête pour mettre à jour les enregistrements phone_number. Si la sous-chaîne « 124 » a été trouvée dans cette colonne, mettez à jour le numéro de téléphone à « 999 ».

-- Rédigez une requête pour trouver les détails des employés dont le prénom contient huit caractères ou plus.

-- Écrivez une requête à joindre en majuscules, la première lettre du prénom, avec le nom de famille, avec ' @example.com ' dans la colonne email.

--   **Sample Output :**
--   EMAIL
--   --------------------

--   JDOE@example.com (where first_name is John, and last_name is Doe)


-- Écrivez une requête pour obtenir l'identifiant de l'employé, envoyez un e-mail, mais supprimez les trois derniers caractères de l'e-mail.


-- Rédigez une requête pour afficher le premier mot du titre du poste, si le titre du poste contient plusieurs mots.

-- Écrivez une requête qui affiche le prénom et la longueur du prénom pour tous les employés dont le nom commence par les lettres 'A', 'J' ou 'M'. Donnez à chaque colonne une étiquette appropriée. Triez les résultats par les prénoms des employés.

-- Rédigez une requête pour afficher le prénom et le salaire de tous les employés. Affichez le salaire avec le symbole $. Intitulez la colonne SALAIRE.
-- A REFAIRE INACHEVE RESTE DES REQUETES

