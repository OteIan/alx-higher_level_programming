-- all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT title, name
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
ORDER BY title, name ASC;
