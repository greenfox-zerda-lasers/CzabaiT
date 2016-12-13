// Add a click event listener to a <button> and console.log its innerHTML
var button = document.querySelector('button');

var counter = 0;

function countIncrement() {
  counter++;
  button.innerHTML = counter;
  console.log(counter);
}

button.addEventListener("click", countIncrement);
