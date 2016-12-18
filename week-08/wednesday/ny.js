var span = document.querySelector("span");
var prev = document.querySelector("#prev_button");
var next = document.querySelector("#next_button");
var apiDoc = '';
var articleHeadline = [];
var articleSnippet = [];
var articlePubDate = [];
var articleNumber = 0;

var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=apollo+11+moon', true);
xhr.send();
xhr.onreadystatechange = function(){
  if(xhr.readyState === XMLHttpRequest.DONE){
    apiDoc = JSON.parse(xhr.response);
    articleLister(apiDoc);
  }
};


function articleLister (apiDoc) {
  apiDoc.response.docs.forEach(function(elem) {
    articleSnippet.push(elem.snippet);
  });
  span.innerHTML = articleSnippet[0];
  console.log(articleSnippet);
  prev.addEventListener("click", prevImage);
  next.addEventListener("click", nextImage);
}

function nextImage() {
  articleNumber++;
  if(articleNumber >= articleSnippet.length) {
    articleNumber = 0;
  }
  span.innerHTML = articleSnippet[articleNumber];
}

function prevImage() {
  articleNumber--;
  if(articleNumber < 0) {
    articleNumber = articleSnippet.length-1;
  }
  span.innerHTML = articleSnippet[articleNumber];
}
