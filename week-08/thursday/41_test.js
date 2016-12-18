var test = require('tape');
var summer = require('./41.js');

var testArray = [4, 5, 6, 7, 8, 9, 10];

test('sum array', function(t) {
  var actual = summer(testArray);
  var expected = 49;

  t.equal(actual, expected);
  t.end();
});
