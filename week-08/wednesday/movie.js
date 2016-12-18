var filmInput = document.querySelector("#film_input");
var ratingInput = document.querySelector("#rating_input");
var answerArray = {};

var submitButton = document.querySelector("#submit_button");
submitButton.addEventListener("click", function(e) {
  e.preventDefault();
  answerArray[filmInput.name] = filmInput.value;
  answerArray[ratingInput.name] = ratingInput.value;
  console.log(answerArray);
});

var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://sheetsu.com/apis/v1.0/7654fbe24554', true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(JSON.stringify(answerArray));
