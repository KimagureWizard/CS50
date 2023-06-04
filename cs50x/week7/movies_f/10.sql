SELECT DISTINCT(name) FROM people
WHERE people.id in (SELECT person_id FROM directors
WHERE movie_id in (SELECT movie_id FROM ratings
WHERE rating > 9));