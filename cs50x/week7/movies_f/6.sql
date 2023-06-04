SELECT AVG(rating) AS [average rating] FROM ratings
WHERE movie_id IN (SELECT id FROM movies WHERE year = 2012);