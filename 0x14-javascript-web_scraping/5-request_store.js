#!/usr/bin/node
const response = require('request');
const f = require('fs');

response.get(process.argv[2]).pipe(f.createWriteStream(process.argv[3]));
