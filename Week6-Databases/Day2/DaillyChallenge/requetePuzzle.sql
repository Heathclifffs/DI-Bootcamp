CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);
INSERT INTO FirstTab VALUES(5,'Pawan'),(7,'Sharlee'),(NULL,'Avtaar');
CREATE TABLE SecondTab(
	id integer
);
INSERT INTO SecondTab VALUES
(5),
(NULL)
-- Q1. Quelle sera la SORTIE de l'instruction suivante ?

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );
-- Retourne zero (0)
-- Q2. Quelle sera la SORTIE de l'instruction suivante ?
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
-- retourne 1

-- Q3. Quelle sera la SORTIE de l'instruction suivante ?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
-- retourne zero
-- Q4. Quelle sera la SORTIE de l'instruction suivante ?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- retourne 1