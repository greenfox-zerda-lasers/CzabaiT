'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rockets(fuelConsumption) {
    this.fuelConsumption =  fuelConsumption;
    this.fuelAmount = 0;
    this.numOfLaunches = 0;
    this.fill = function(amount) {
      this.fuelAmount += amount;
    };
    this.launch = function() {
      if (this.fuelAmount >= this.fuelConsumption) {
        this.fuelAmount -= this.fuelConsumption;
        this.numOfLaunches += 1;
        return console.log("Num of launches: " + this.numOfLaunches);
      } else{
        console.log("Not enough fuel to launch");
      }
    };

}

var rocket = new Rockets(40);

rocket.launch();
rocket.fill(50);
rocket.launch();
console.log(rocket.fuelAmount);
