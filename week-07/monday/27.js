'use strict';

var z = 13;
// if z is between 10 and 20 print 'Sweet!'
// if less than 10 print 'More!',
// if more than 20 print 'Less!'

function numberChecker(number) {
  if (number < 10) {
    console.log('More!');
  } else if (number > 20) {
    console.log('Less!');
  } else{
    console.log('Sweet');
  }
}

console.log(numberChecker(z));
