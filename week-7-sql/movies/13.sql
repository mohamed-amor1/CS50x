/*
-- write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
-- Your query should output a table with a single column for the name of each person.
-- There may be multiple people named Kevin Bacon in the database. Be sure to only select the Kevin Bacon born in 1958.
-- Kevin Bacon himself should not be included in the resulting list.


*/

.schema
SELECT DISTINCT people.name
FROM people
JOIN stars AS s1 ON s1.person_id = people.id
JOIN movies AS m1 ON m1.id = s1.movie_id
JOIN stars AS s2 ON s2.movie_id = m1.id
JOIN people AS p2 ON p2.id = s2.person_id AND p2.name = 'Kevin Bacon' AND p2.birth = 1958
WHERE people.name != 'Kevin Bacon'
ORDER BY people.name;


