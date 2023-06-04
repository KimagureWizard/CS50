SELECT AVG(energy) AS [average energy] FROM songs
WHERE artist_id IN (SELECT id FROM artists WHERE name="Drake");