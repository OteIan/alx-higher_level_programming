#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) console.error(error);

  const films = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;

    for (let j = 0; j < characters.length; j++) {
      if (characters[j].endsWith('/18/')) count++;
    }
  }
  console.log(count);
});
