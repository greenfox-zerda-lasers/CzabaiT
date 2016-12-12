'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animals(animalSound) {
  this.animalSound = animalSound;
  this.say = function() {
    console.log(this.animalSound);
  };
}

/*Animals.prototype.say = function () {
  console.log(this.animalSound);
};*/

var kecske = new Animals("meeee");
kecske.say();
