/*
audio aura : average of energy, valence, and danceability of a person’s top 100 songs from the past year
*/
.schema

SELECT AVG(energy), AVG(valence), AVG(danceability) FROM songs;
SELECT AVG(energy + valence + danceability) AS overall_avg FROM songs;