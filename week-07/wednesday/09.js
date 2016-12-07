'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function letterLister (string) {
  var letterList = {};

   for(var i = 0; i < string.length; i++){
       var item = string[i];
       letterList[item] = (letterList[item] +1 ) || 1;
   }
   return letterList;
}


function letterReducer (string) {
  return string.reduce(function(acc,char){
      acc[char] = (acc[char] + 1) || 1;
      return acc;
  }, {});
}

console.log(letterLister('dvjjassihvv9'));
console.log(letterReducer('dvjjassihvv9'));
