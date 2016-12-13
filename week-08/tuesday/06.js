// Add an event listener to the window and display the mouse's x, y coordinates

var posStats = document.getElementById('pos-stats');
var xPos, yPos;

document.onmousemove = function(e) {
  xPos = e.pageX;
  yPos = e.pageY;
};

function showSomething() {
  posStats.innerHTML = "Pos: x: " + xPos + " y: " + yPos;
}


window.addEventListener("mouseover", showSomething);
