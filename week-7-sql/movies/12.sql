/*
-- Write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
-- Your query should output a table with a single column for the title of each movie.
-- You may assume that there is only one person in the database with the name Johnny Depp.
-  You may assume that there is only one person in the database with the name Helena Bonham Carter.

*/

.schema
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Johnny Depp"
INTERSECT
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter"
ORDER BY movies.title;

/*
Your code first joins the people, stars, and movies tables together to get all the movies in which Johnny Depp starred, and then does the same to get all the movies in which Helena Bonham Carter starred. The INTERSECT operator then combines these two sets of movies and returns only the movies that appear in both sets, i.e. the movies in which both Johnny Depp and Helena Bonham Carter starred. Finally, the SELECT statement selects only the titles of these movies.

*/