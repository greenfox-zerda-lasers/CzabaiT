// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

function tour (walk, distance, length) {
  return walk(distance(length));
}

function walk (array) {
  array.fill(true);
  return array;
}

function distance (length) {
  var array = [];
  for(var i = 0; i < length; i++) {
    array.push(false);
  }
  return array;
}

console.log(tour(walk, distance, 5));
