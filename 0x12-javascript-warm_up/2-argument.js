#!/usr/bin/node

const { argv } = require('node:process');

if (length(argv) == 0)
    console.log("No arguments found");
else if (length(argv) == 1)
    console.log("argument found");
else
    console.log("arguments found");
