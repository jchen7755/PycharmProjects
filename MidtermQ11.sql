USE movierental;

SELECT * FROM Movie;

SELECT movie_id, title 
FROM Movie 
ORDER BY year DESC;

SELECT title 
FROM Movie 
WHERE year <= 2003;

SELECT DISTINCT m.movie_id, m.title
FROM Movie m
JOIN MovieGenre mg ON m.movie_id = mg.movie_id
JOIN Genre g ON mg.genre_id = g.genre_id
WHERE g.name IN ('Drama', 'Horror');

SELECT title, year 
FROM Movie
WHERE year < 2000 OR year > 2010
ORDER BY year ASC;

SELECT title, year 
FROM Movie
WHERE year <> 2003
ORDER BY year DESC;

SELECT g.name, COUNT(*) AS num_movies
FROM Genre g
JOIN MovieGenre mg ON g.genre_id = mg.genre_id
GROUP BY g.name;

SELECT DISTINCT c.first_name, c.last_name
FROM Customer c
JOIN Rental r ON c.membership_id = r.membership_id
JOIN Video v ON r.video_id = v.video_id
JOIN Movie m ON v.movie_id = m.movie_id
WHERE m.title = 'Lord of the rings: fellowship of the ring';

SELECT DISTINCT c.membership_id, c.first_name, c.last_name
FROM Customer c
JOIN Rental r ON c.membership_id = r.membership_id
WHERE r.check_in_date IS NULL;

SELECT DISTINCT m.title, 
       CONCAT(d.first_name, ' ', d.last_name) AS director_name
FROM Movie m
JOIN MovieDirector md ON m.movie_id = md.movie_id
JOIN Director d ON md.director_id = d.director_id
WHERE m.movie_id IN (
    SELECT movie_id FROM MovieDirector
    GROUP BY movie_id HAVING COUNT(*) > 1
)
AND m.movie_id IN (
    SELECT movie_id FROM MovieGenre
    GROUP BY movie_id HAVING COUNT(*) > 1
);

ALTER TABLE Actor ADD national VARCHAR(50);

INSERT INTO Actor (actor_id, first_name, last_name) VALUES
(1, 'Will', 'Smith'),
(2, 'Tom', 'Hanks'),
(3, 'Leonardo', 'DiCaprio'),
(4, 'Angelina', 'Jolie'),
(5, 'Marilyn', 'Monroe');

SET SQL_SAFE_UPDATES = 0;
UPDATE Actor SET national = 'American';
SET SQL_SAFE_UPDATES = 1;






