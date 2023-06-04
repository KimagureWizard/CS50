SELECT COUNT(title) AS numbers FROM movies
WHERE id IN (SELECT movie_id FROM ratings WHERE rating = 10);