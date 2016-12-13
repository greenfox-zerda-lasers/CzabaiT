// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

var posStats = document.getElementById('pos-stats');
var xPos, yPos;

document.onmousemove = function(e) {
  xPos = e.pageX;
  yPos = e.pageY;
};

function showSomething() {
  posStats.innerHTML = "Pos: x: " + xPos + " y: " + yPos;
}

setInterval(showSomething, 1500);


/*(function() {
    var mousePos;
    var posStats = document.getElementById('pos-stats');

    document.onmousemove = handleMouseMove;
    setInterval(getMousePosition, 1500);

    function handleMouseMove(event) {
        var pageX, pageY;

        mousePos = {
            x: event.pageX,
            y: event.pageY
        };
    }

    function getMousePosition() {
        var pos =mousePos;
        if (!pos) {
          posStats.innerHTML = "Pos: Mozdulj má' meg";
        }
        else {
          posStats.innerHTML = "Pos: x: " + mousePos["x"] + " y: " + mousePos["y"];
        }
    }
})();*/
