'esversion: 6';
// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function inheritPrototype(childObject, parentObject) {
   var copyOfParent = Object.create(parentObject.prototype);
   copyOfParent.constructor = childObject;
   childObject.prototype = copyOfParent;
}

function Aircraft() {
  this.type = "";
  this.ammo = 0;
  this.baseDamage = 0;
  this.allDamage = 0;
  this.maxAmmo = 0;
}

Aircraft.prototype = {
    constructor: Aircraft,

    fight: function() {
      this.allDamage = this.ammo * this.baseDamage;
      this.ammo = 0;
    },

    refill: function(refillAmount) {
      this.excessAmmo = (this.ammo + refillAmount) - this.maxAmmo;
      if (this.excessAmmo > 0) {
        this.ammo = this.maxAmmo;
        return this.excessAmmo;
      } else{
        this.ammo += refillAmount;
        return 0;
      }
    },

    checkState: function() {
      return "Type " + this.type + ", Ammo: " + this.ammo + ", Base Damage: " + this.baseDamage + ", All Damage: " + this.allDamage;
    }
};

function F16() {
  Aircraft.call(this);
  this.type = "F16";
  this.maxAmmo = 8;
  this.baseDamage = 30;
}

inheritPrototype(F16, Aircraft);

function F35() {
  Aircraft.call(this);
  this.type = "F35";
  this.maxAmmo = 12;
  this.baseDamage = 50;
}

inheritPrototype(F35, Aircraft);


function Carrier(totalAmmo) {
  this.totalAmmo = totalAmmo;
  this.health = 3000;
  this.count = 0;
  this.totalDamage = 0;
  this.planes = [];
}

Carrier.prototype = {
  constructor: Carrier,

  checkState: function() {
    return "Aircraft count: " + this.count + ", Ammo Storage: " + this.totalAmmo + ", Total Damage: " + this.totalDamage + ", Health Remaining: " + this.health;
  },

  statusReport: function() {
    if(this.health > 0) {
      this.allPlanesStatus = "";
      for(var plane in this.planes) {
        this.allPlanesStatus += "\n" + this.planes[plane].checkState();
      }
      return this.checkState() + "\n Aircrafts:" + this.allPlanesStatus;
    } else{
      return "It\'s dead Jim :(";
    }
  },

  addAircraft: function(current_plane) {
    this.planes.push(current_plane);
  },

  fill: function() {
    for(var plane in this.planes) {
      if(this.totalAmmo > 0) {
          this.totalAmmo = this.planes[plane].refill(this.totalAmmo);}
    }
  },

  fight: function() {
    for(var plane in this.planes) {
      this.planes[plane].fight();
      this.totalDamage += this.planes[plane].allDamage;}
  }
};

var plane1 = new F16();
var plane2 = new F16();
var plane3 = new F35();
var carrier = new Carrier(720);
carrier.addAircraft(plane1);
carrier.addAircraft(plane2);
carrier.addAircraft(plane3);


console.log(carrier.planes);
console.log(carrier.fill());
console.log(carrier.planes);
console.log(carrier.fight());
console.log(carrier.planes);

console.log(carrier.statusReport());
