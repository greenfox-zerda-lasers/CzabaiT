// Based on the previous example create an array of images taken from flickr
// https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/

// Display a progress bar while the images are loading
// You can create your own or use the built in HTML5 version:
// https://developer.mozilla.org/en/docs/Web/HTML/Element/progress

var imagesSource = [
 'https://c7.staticflickr.com/8/7799/26683911430_c4662bf0ec_c.jpg',
 'https://c2.staticflickr.com/9/8574/16635664865_9f5e9e2918_c.jpg',
 'https://c5.staticflickr.com/3/2929/14195441260_7201745aaa_c.jpg',
];

var parentContent = document.querySelector("body");

for(var i = 0; i < 3; i++) {
  var newImg = document.createElement("img");
  newImg.src = imagesSource[i];
  newImg.id = "img" + i;
  newImg.visibility = "hidden";
  parentContent.appendChild(newImg);
}

var images = document.querySelectorAll("img");
for(var image of images) {
  image.addEventListener("load", function(event) {
    image.visibility = "visible";
  });
}
