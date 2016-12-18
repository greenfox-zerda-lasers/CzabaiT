var test = require('tape');
var appender = require('./40.js');



test('append "a" to string', function (t) {
    var actual = appender('marh');
    var expected = "marha";

    t.equal(actual, expected);
    t.end();
});
