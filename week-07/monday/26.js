'use strict';

var y = 'seasons';
var out = 6;
// if the last and the first letter of the string
// are the same double the variable
// called out, if not half it

function stringSidesChecker (string) {
  if (string[0] === string[string.length-1]) {
    out *= 2;
  } else{
    out /= 2;
  }
  return out;
}

console.log(stringSidesChecker(y));
