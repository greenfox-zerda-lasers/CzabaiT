'use strict'

var aj = 'kuty'
// write a function that gets a string as an input
// and appends an 'a' character to its end and returns a new string

function Appender(string) {
  aj += 'a'
  return aj
}

console.log(Appender(aj));
