#!/usr/bin/node
let num = parseInt(process.argv[2]);

if (isNaN(num)) {
    console.log('Missing size');
}

for (let i = 1; i <= num ; i++) {
    for (let j = 1; j <= num; i++) {
        console.log('x');
    }
}
