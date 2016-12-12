'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function oddFilter(array) {
  var new_array = [];
  for(var i = 0; i < array.length; i++) {
      if(array[i] % 2 === 1) {
        new_array.push(array[i]);
      }
  }
  return new_array;
}

console.log(oddFilter(numbers));
