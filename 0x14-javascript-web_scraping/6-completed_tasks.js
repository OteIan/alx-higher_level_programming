#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) console.error(error);
  else {
    const work = JSON.parse(body);
    const result = {};
    
    work.forEach((task) => {
      if (task.result && result[task.userId] === undefined) {
        result[task.userId] = 1;
      } else if (task.result) {
        result[task.userId]++;
      }
    });
    console.log(result);
  }
});
