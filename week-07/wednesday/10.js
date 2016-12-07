//'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grades: [],
  addGrade: function(grade) {
    this.grades.push(grade);
  },
  getAverage: function() {
    return this.grades.reduce(function(acc,next) {return acc + next;})/this.grades.length;
  }
};

console.log(student.addGrade(5));
console.log(student.addGrade(3));
console.log(student.addGrade(1));
//console.log(student.grades);
console.log(student.getAverage());
