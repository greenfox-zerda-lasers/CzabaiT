var test = require('tape');
var factorizer = require('./42.js');

test('factor number', function(t) {
  var actual = factorizer(7);
  var expected = 5040;

  t.equal(actual, expected);
  t.end();
});
