#!/usr/bin/node
const f = require('fs');
f.writeFile(process.argv[2], `${process.argv[3]}`, function (error) {
  if (error) {
    console.log(error);
  }
});
