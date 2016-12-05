'use strict';

var j1 = 10;
var j2 = 3;
// tell if j1 is higher than j2 squared
// and smaller than j2 cubed

var whether = j1 > Math.pow(j2, 2) && j1 < Math.pow(j2, 3);
console.log(whether);
