-- Tous les articles, classés par prix (du plus bas au plus élevé).
SELECT * FROM items ORDER BY Prix ASC;
-- Articles dont le prix est supérieur à 80 (80 inclus), classés par prix (du plus élevé au plus bas).
SELECT * FROM items WHERE Prix>=80 ORDER BY Prix DESC;