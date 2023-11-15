#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const a = process.argv[2];
const b = process.argv[3];

const sum = add(a, b);
console.log(sum);
