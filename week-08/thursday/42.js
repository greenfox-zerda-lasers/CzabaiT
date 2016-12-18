'use strict';

// create a function that returns it's input factorial

var factorizer = function(number) {
  var factor = 1;
  while(number > 0) {
    factor *= number;
    number--;
  }
  return factor;
};


module.exports = factorizer;
