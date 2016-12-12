var newLi = document.createElement("li");
newLi.textContent = "The Green Fox";

var parentUl = document.querySelector('.asteroids');

parentUl.appendChild(newLi);


var newImg = document.createElement("img");
newImg.setAttribute('src', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/H%C3%A1zikecske_portr%C3%A9.JPG/250px-H%C3%A1zikecske_portr%C3%A9.JPG');
document.querySelector('.container').appendChild(newImg);
