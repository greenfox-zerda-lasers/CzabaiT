// Embed the following file to a HTML document:
//  - From the previous flickr example extract the .jpg link directly
//  - Create an image tag in the with document.createElement
//  - Add a 'load' event to the image and only show the image to the user when the image is loaded



var parentContent = document.querySelector("body");

var newImg = document.createElement("img");
newImg.src = "https://c7.staticflickr.com/8/7562/15584243094_2e25d9c978_c.jpg";
newImg.visibility = "hidden";
newImg.id = "img0";
parentContent.appendChild(newImg);

var img0 = document.querySelector("#img0");
img0.addEventListener("load", function(event) {
  img0.visibility = "visible";
});
