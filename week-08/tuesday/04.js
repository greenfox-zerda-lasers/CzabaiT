// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

var posStats = document.getElementById('pos-stats');
var xPos, yPos;

document.onmousemove = function(e) {
  xPos = e.pageX;
  yPos = e.pageY;
};

function showSomething() {
  posStats.innerHTML = "Pos: x: " + xPos + " y: " + yPos;
  setTimeout(showSomething, 1500);
}

showSomething();
