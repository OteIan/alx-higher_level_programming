#!/usr/bin/node
const f = require('fs');
f.readFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
