'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack() {
  this.elements = [];
  this.size = function() {
    return this.elements.length;
  };
  this.push = function(element) {
    this.elements.push(element);
  };
  this.pop = function() {
    this.lastElement = this.elements.pop();
    return this.lastElement;
  };
}

var stack = new Stack();

console.log(stack.size());
stack.push(3);
stack.push('alma');
console.log(stack.size());
console.log(stack.pop());
console.log(stack.size());
