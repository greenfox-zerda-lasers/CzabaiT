//'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function letterInStringChecker(string, letter) {
  return string.indexOf(letter) != -1;
}

console.log(letterInStringChecker('Béla', 'é'));
console.log(letterInStringChecker('Béla', 'k'));
