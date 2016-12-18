var test = require('tape');
var minimalFinder = require('./44.js');

var testArray = [7, 5, 8, -1, 2];

test('Find minimal value of arry', function(t) {
  var actual = minimalFinder(testArray);
  var expected = -1;

  t.equal(actual, expected);
  t.end();
});
