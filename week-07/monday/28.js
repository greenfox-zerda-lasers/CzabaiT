'use strict';

var aa = [1, 2, 3];
var out = 0;
// if the aa list contains one element set the out to 1
// if the aa list contains two elements set the out to 2
// if the aa list contains more than 2 set the out to 10
// if the aa contains no elements set out to -1

function listLengthChecker (list) {
  var length = list.length;
  switch (length) {
    case 0:
      out = -1;
      break;
    case 1:
      out = 1;
      break;
    case 2:
      out = 2;
      break;
    default:
      out = 10;
      break;
  }
  return out;
}

console.log(listLengthChecker(aa));
