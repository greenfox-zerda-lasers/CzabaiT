'use strict';

var ah = ['kuty', 'macsk', 'cic']
// add to all elements an 'a' on the end

function  aLetterExpander(list) {
  var new_list = []
  list.forEach(function(element, index) {
    list[index] = (element + 'a');
  });
  return list;
}

console.log(aLetterExpander(ah));
console.log(ah);
