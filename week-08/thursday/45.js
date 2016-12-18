'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

var shortestStringChooser = function(array) {
  var shortestName = array[0];
  array.forEach(function(item) {
    if(shortestName.length > item.length) {
      shortestName = item;
    }
  });
  return shortestName;
};

module.exports = shortestStringChooser;
