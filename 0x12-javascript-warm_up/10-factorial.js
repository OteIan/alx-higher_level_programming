#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  let factorial = 1;
  if (isNaN(num)) {
    return 1;
  }

  for (let i = 1; i <= num; ++i) {
    factorial *= i;
  }
  return factorial;
}

const fact = factorial(num);
console.log(fact);
