'use strict';

var x = 'cheese';
// Tell if the x has even or odd number of
// characters with a true for even and
// false output otherwise

function evenOrOdd (string) {
  if (string.length % 2 === 0) {
    return true;
  } else{
    return false;
  }
}

console.log(evenOrOdd(x));
