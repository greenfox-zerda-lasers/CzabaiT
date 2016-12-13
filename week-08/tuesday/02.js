// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout


function delayedAlert() {
  alert("I\'m delayed");
}

var timeOutId = setTimeout(delayedAlert, 3000);


function cancelSetTimeout() {
  clearTimeout(timeOutId);
}

var cancelButton = document.getElementById("cancel-button");
cancelButton.addEventListener("click", cancelSetTimeout);
