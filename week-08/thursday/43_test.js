var test = require('tape');
var oddFilter = require('./43.js');

var testArray = [3, 4, 5, 6, 7];
var expectedArray = [4, 6];

test('Filter out odd numbers from an array', function(t) {
  var actual = oddFilter(testArray);
  var expected = expectedArray;

  t.deepEqual(actual, expected);
  t.end();
});
