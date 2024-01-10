$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  for (const movie in data.results) {
    $('#list_movies').append('<li>' + data.results[movie].title + '</li>');
  }
});
