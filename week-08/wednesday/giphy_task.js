var response = '';
var numOfPics = 16;
var parentBody = document.querySelector("body");

var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+bunny&api_key=dc6zaTOxFJmzC', true); // Also try http://444.hu/feed
xhr.send();
xhr.onreadystatechange = function(){
  if(xhr.readyState === XMLHttpRequest.DONE){
    response = JSON.parse(xhr.response);

    imgMaker(response);
  }
};

function imgMaker (response) {
  response.data.forEach(function(elem, index) {
    var img = document.createElement("img");
    img.id = "img" + index;
    var imgMoving = elem.images.original.url;
    var imgStill = elem.images.original_still.url;
    img.src = imgStill;
    img.addEventListener("mouseout", function(){img.src = imgStill;});
    img.addEventListener("mouseover", function(){img.src = imgMoving;});
    parentBody.appendChild(img);
  });
}
