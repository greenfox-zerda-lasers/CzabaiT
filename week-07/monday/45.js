'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortestStringChooser(array) {
  var shortest = array[0];
  for(var i = 1; i < array.length; i++) {
    if(shortest.length > array[i].length) {
      shortest = array[i];
    }
  }
  return shortest;
}

console.log(shortestStringChooser(names));
