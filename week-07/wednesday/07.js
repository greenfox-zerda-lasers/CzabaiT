'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrime(number) {
  for (var i = 2; i <= Math.floor(number/2); i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

function primeEveryChecker(array) {
  return array.every(function(e) {return isPrime(e);})
}

console.log(primeEveryChecker(numbers));
console.log(primeEveryChecker([3,5,7]));
