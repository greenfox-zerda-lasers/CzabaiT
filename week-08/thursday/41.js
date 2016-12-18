'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function

var summer = function(array) {
  var sum = 0;
  array.forEach(function(item) {
      sum += item;
    }
  );
  return sum;
};


module.exports = summer;
