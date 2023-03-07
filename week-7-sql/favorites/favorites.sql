-- SQLite
.schema

SELECT * FROM shows;

UPDATE shows SET title = "How I Met Your Mother" WHERE title = "How i met your mother";

SELECT * FROM shows;

UPDATE shows SET title = "Brooklyn Nine-Nine" WHERE title LIKE "Br%";

UPDATE shows SET title = "The Office" WHERE title LIKE "%Office";

UPDATE shows SET title = "The Untamed" WHERE title LIKE "%untamed";

UPDATE shows SET title = "Sherlock" WHERE title LIKE "sherl%";

UPDATE shows SET title = "Grey’s Anatomy" WHERE title LIKE "%grey%";

UPDATE shows SET title = "Friends" WHERE title LIKE "%friend%";

UPDATE shows SET title = "It’s Always Sunny in Philadelphia" WHERE title LIKE "%Sunny%";  

UPDATE shows SET title = "Avatar: The Last Airbender" WHERE title LIKE "%avatar%"; 

UPDATE shows SET title = "Brooklyn Nine-Nine" WHERE title LIKE "%99%";

UPDATE shows SET title = "Family Guy" WHERE title LIKE "%family%";

UPDATE shows SET title = "Arrow" WHERE title LIKE "%arrow%";

UPDATE shows SET title = "Community" WHERE title LIKE "%community%";

UPDATE shows SET title = "The Bachelorette" WHERE title LIKE "%bachelor%"; 

UPDATE shows SET title = "The Crown" WHERE title LIKE "%crown%";

UPDATE shows SET title = "Game of Thrones" WHERE title LIKE "%got%";

UPDATE shows SET title = "Billions" WHERE title LIKE "%billion%";

UPDATE shows SET title = "Criminal Minds" WHERE title LIKE "%criminal%";

UPDATE shows SET title = "Squid Game" WHERE title LIKE "%squid%";

UPDATE shows SET title = "Parks and Recreation" WHERE title LIKE "%park%";

UPDATE shows SET title = "The Queen’s Gambit" WHERE title LIKE "%gambi%";



SELECT * FROM shows;