function Ajax() {
}

Ajax.prototype = {
  constructor: Ajax,

  openDatabase: function(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
    xhr.send();
    xhr.onreadystatechange = function(){
      if(xhr.readyState === XMLHttpRequest.DONE){
        var serverAnswer = JSON.parse(xhr.response);
        callback(serverAnswer);
      }
    };
  },

  deleteDatabase: function(id) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
    xhr.send();
  },

  putDatabase: function(text, id, completed) {
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
    xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"text": text, "completed": completed}));
    console.log("lefutott a put");
  },

  postDatabase: function(text) {
    if(text === ""){
      return;
    }
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
    xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"text": text}));
  },
};

function App() {
  this.ajax = new Ajax();
  this.initLoad = this.ajax.openDatabase(this.listDatabase);
}

App.prototype = {
  constructor: App,

  parentUl: document.querySelector("#todo-list-ul"),

  addTodoItem: function(id, text, completed) {
    var listItem = document.createElement("li");
    this.parentUl.appendChild(listItem);
    var textDiv = document.createElement("div");
    textDiv.classList.add("todo-text");
    listItem.appendChild(textDiv);
    var textP = document.createElement("p");
    textDiv.appendChild(textP);

    if(text === ""){
      textP.innerHTML = "%/$ß@&#!";
    } else{
      textP.innerHTML = text;
    }

    var commandsDiv = document.createElement("div");
    commandsDiv.classList.add("todo-commands");
    listItem.appendChild(commandsDiv);
    var binButtonDiv = document.createElement("div");
    binButtonDiv.classList.add("bin-button");
    commandsDiv.appendChild(binButtonDiv);
    binButtonDiv.innerHTML = "&#10008;";
    var checkButtonDiv = document.createElement("div");
    checkButtonDiv.classList.add("check-button");
    checkButtonDiv.classList.add(completed);
    commandsDiv.appendChild(checkButtonDiv);
    checkButtonDiv.innerHTML = "&#10004;";

    binButtonDiv.addEventListener("click",function(){
      console.log(id);
      this.ajax.deleteDatabase(id);
//    this.ajax.openDatabase(this.listDatabase);
    }.bind(this));

    var completedChange = !completed;
    checkButtonDiv.addEventListener("click",function(){
      this.ajax.putDatabase(text, id, completedChange);
//    this.ajax.openDatabase(this.listDatabase);
    }.bind(this));
  },

  listDatabase: function(serverAnswer) {
    serverAnswer.forEach(function(item) {
      app.addTodoItem(item.id, item.text, item.completed);
    });
    console.log("lefutott a listázás");
  }
};

var app = new App();

var inputButton = document.querySelector("button");

inputButton.addEventListener("click", function(){
  var inputField = document.querySelector("input");
  app.ajax.postDatabase(inputField.value);
//  app.ajax.openDatabase(app.listDatabase);
});


// ---------------BONUS---------------


var requestAnimationFrame = window.requestAnimationFrame;

var inputButtonText = document.querySelector("#input-button-text");

var currentPos = 0;

function animateButtonText() {
  currentPos += 2;
  if(currentPos === 0) {
    return;
  }
  inputButtonText.style.left = currentPos + "px";

  if(Math.abs(currentPos) >= 100) {
    currentPos = -50;
  }
  requestAnimationFrame(animateButtonText);
}

inputButton.addEventListener("click", animateButtonText);
