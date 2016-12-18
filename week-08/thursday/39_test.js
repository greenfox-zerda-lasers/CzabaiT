var test = require('tape');
var doubler = require('./39.js');



test('double input', function (t) {
    var actual = doubler(33);
    var expected = 66;

    t.equal(actual, expected);
    t.end();
});
