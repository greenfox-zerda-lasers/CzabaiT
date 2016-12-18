'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function isEven(number) {
  return number % 2 === 0;
}

var oddFilter = function(array) {
    var filteredArray = array.filter(isEven);
    return filteredArray;
};

// console.log(typeof(numbers));
// console.log(typeof(oddFilter(numbers)));

module.exports = oddFilter;
