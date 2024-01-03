#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) console.error(error);

  const actors = JSON.parse(body).characters;

  for (let j = 0; j < actors.length; j++) {
    //   if (actors[j].endsWith('/18/')) count++;
    request(actors[j], function (error, response, body) {
      if (error) console.error(error);
      console.log(JSON.parse(body).name);
    });
  }
});
