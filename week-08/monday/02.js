'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangles(height, width) {
  this.height = height;
  this.width = width;
  this.getArea = function() {
    return this.height * this.width;
  };
  this.getCircumference = function() {
    return 2 * (this.height + this.width);
  };
}

var rectangle = new Rectangles(30, 40);
console.log(rectangle.getArea());
console.log(rectangle.getCircumference());
