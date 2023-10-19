-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE title = 'Dexter'
ORDER BY name ASC;
