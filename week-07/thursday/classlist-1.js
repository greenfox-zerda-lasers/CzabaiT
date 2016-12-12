
var  paragraphs = document.querySelectorAll('p');

if (paragraphs[2].hasAttribute('class')) {
  alert('YEAH CAT!');
}

if (paragraphs[3].className === 'dolphin') {
  paragraphs.forEach(function(item) {
//    console.log(item.getAttribute('class'))
    if (item.className === 'apple') {
      item.textContent = 'pear';}
  });
}

paragraphs.forEach(function(item) {
  if (item.className === 'apple') {
    item.className = 'red';}
});
