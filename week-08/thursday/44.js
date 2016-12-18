'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

var minimalFinder = function(array) {
    var minimum = array[0];
    array.forEach(function(item) {
      if (minimum > item) {
        minimum = item;
      }
    });
    return minimum;
};

module.exports = minimalFinder;
