var test = require('tape');
var shortestStringChooser = require('./45.js');

var testArray = ['Béla', 'Károly', 'Lee', 'Lea'];

test('Filter out odd numbers from an array', function(t) {
  var actual = shortestStringChooser(testArray);
  var expected = 'Lee';

  t.equal(actual, expected);
  t.end();
});
