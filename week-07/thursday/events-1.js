var backGround = document.querySelector('div');
var button = document.querySelector('button');

  function partySwitcher () {
    backGround.classList.toggle("party");
    }

button.addEventListener('click', partySwitcher);
