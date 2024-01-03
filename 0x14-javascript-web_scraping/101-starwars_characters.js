#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) console.error(error);

  const actors = JSON.parse(body).characters;
  printCharacters(actors, 0);
});

function printCharacters (actors, index) {
  request(actors[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < actors.length) printCharacters(actors, index + 1);
    }
  });
}
