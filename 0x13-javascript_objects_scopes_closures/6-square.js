#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let chars = '';
      for (let j = 0; j < this.width; j++) {
        chars += c;
      }
      console.log(chars);
    }
  }
}

module.exports = Square;
