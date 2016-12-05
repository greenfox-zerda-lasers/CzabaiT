'use strict';

var ag = [3, 4, 5, 6, 7];
// double all the element's values in ag

function listElementDoubler(list) {
  var new_list = [];
  for (var i = 0; i < list.length; i++) {
    new_list[i] = 2 * list[i];
  }
  return new_list;
}

console.log(listElementDoubler(ag));
