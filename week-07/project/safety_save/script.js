var images = [
  {
    'src': 'images/first.jpg',
    'title': 'in the nature',
    'description' : '\'photohunting\' for birds and horses'
  },
  {
    'src': 'images/second.jpg',
    'title': 'sunny summer',
    'description' : 'chill in Italy'
  },
  {
    'src': 'images/third.jpg',
    'title': 'after accident',
    'description' : 'traffic sign : CT        1 : 0'
  },
  {
    'src': 'images/fourth.jpg',
    'title': 'new year\'s eve',
    'description' : 'we shot down the party at 0:01'
  },
  {
    'src': 'images/fifth.jpg',
    'title': 'ball',
    'description' : 'back to 50\'s'
  }
];

var themes = [
  /*'#0C1836'*/ "style_navy.css",
  /*'#E01A4F'*/ "style_rose.css",
  /*'#F15946'*/ "style_light_rose.css",
  /*'#F9C22E'*/ "style_gold.css",
  /*'#53B3CB'*/ "style_light_navy.css"
];

var img_num = 0;
var theme_num = 0;

var slider = document.getElementById('slider');
var mainTitle = document.getElementById('main_title');
var imgDescription = document.getElementById('img_description');

(function setUp() {

  var thumbnails_title = document.querySelectorAll('.thumbnails');
  thumbnails_title.forEach(function(item, index) {
    item.title = images[index]['title'];
  });

  var theme_button = document.querySelector('.theme_button');
  theme_button.addEventListener("click", nextTheme);

  var thumbIds = document.querySelectorAll('.thumbnails .photos');
  thumbIds.forEach(function(item) {
    item.addEventListener("click", chooseImg);
  });
})();

function chooseImg () {
   img_num = parseInt(this.dataset.thumbId);
   slider.src = images[img_num]['src'];
   mainTitle.innerHTML = images[img_num]['title'];
   imgDescription.innerHTML = images[img_num]['description'];
}

document.onkeydown = navigateKey;

function navigateKey(e) {
    e = window.event;
    if (e.keyCode == '37') {
       prevImage();
    } else if (e.keyCode == '39') {
       nextImage();
    } else if (e.keyCode == '38') {
       prevTheme();
    } else if (e.keyCode == '40') {
       nextTheme();
    }
}

function nextImage() {
  img_num++;
  if(img_num >= images.length) {
    img_num = 0;
  }
  slider.src = images[img_num]['src'];
  mainTitle.innerHTML = images[img_num]['title'];
  imgDescription.innerHTML = images[img_num]['description'];
}

function prevImage() {
  img_num--;
  if(img_num < 0) {
    img_num = images.length-1;
  }
  slider.src = images[img_num]['src'];
  mainTitle.innerHTML = images[img_num]['title'];
  imgDescription.innerHTML = images[img_num]['description'];
}

function nextTheme() {
  theme_num++;
  if(theme_num >= themes.length) {
    theme_num = 0;
  }
  theme_css.href = themes[theme_num];
}

function prevTheme() {
  theme_num--;
  if(theme_num < 0) {
    theme_num = themes.length-1;
  }
  theme_css.href = themes[theme_num];
}


/*
function chooseImg() {
  var imgId = this.id;
  switch (imgId) {
    case "first_thumbnail":
      img_num = 0;
    case "second_thumbnail":
      img_num = 1;
    case "third_thumbnail":
      img_num = 2;
    case "fourth_thumbnail":
      img_num = 3;
    case "fifth_thumbnail":
      img_num = 4;
  slider.src = images[img_num]['src'];
  }
}
*/

/*function first() {
  img_num = 0;
  slider.src = images[img_num]['src'];
}

function second() {
  img_num = 1;
  slider.src = images[img_num]['src'];
}

function third() {
  img_num = 2;
  slider.src = images[img_num]['src'];
}

function fourth() {
  img_num = 3;
  slider.src = images[img_num]['src'];
}

function fifth() {
  img_num = 4;
  slider.src = images[img_num]['src'];
}*/
