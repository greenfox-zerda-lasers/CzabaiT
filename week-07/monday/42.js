'use strict';

// create a function that returns it's input factorial

function Factorizer(number) {
  var i = number;
  var factorial = 1;
  while(i > 0) {
    factorial *= i;
    i--;
  }
  return factorial;
}

console.log(Factorizer(5));
