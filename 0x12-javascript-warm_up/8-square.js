#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
}

for (let i = 1; i <= num; i++) {
  let characters = '';
  for (let j = 1; j <= num; j++) {
    characters += 'X';
  }
  console.log(characters);
}
