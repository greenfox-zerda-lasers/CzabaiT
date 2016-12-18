// Create a circle with 100px diameter (use border radius)
//  - Make it move from left to right edge
//  - use requestAnimationFrame

var requestAnimationFrame = window.requestAnimationFrame;

var donut = document.querySelector("#donut");
var donutContainer = document.querySelector("#donut-container");

var currentPos = 40;

function animateDonut() {
  currentPos += 5;
  // if(currentPos === 40) {
  //   return;
  // }
  donut.style.left = currentPos + "px";

  if(Math.abs(currentPos) >= 700) {
    currentPos = -300;
  }
  requestAnimationFrame(animateDonut);
}

donutContainer.addEventListener("click", function(){
  animateDonut();});

//function(){console.log("Béla");}
