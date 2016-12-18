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

  deleteDatabase: function(id, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
    xhr.send();
    xhr.onreadystatechange = function(){
      if(xhr.readyState === XMLHttpRequest.DONE){
        var serverAnswer = JSON.parse(xhr.response);
        callback(serverAnswer);
      }
    };
  },

  putDatabase: function(text, id, completed, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("PUT", 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id, true);
    xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"text": text, "completed": completed}));
    console.log("lefutott a put");
    xhr.onreadystatechange = function(){
      if(xhr.readyState === XMLHttpRequest.DONE){
        var serverAnswer = JSON.parse(xhr.response);
        callback(serverAnswer);
      }
    };
  },

  postDatabase: function(text, callback) {
    if(text === ""){
      return;
    }
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
    xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
    xhr.send(JSON.stringify({"text": text}));
    xhr.onreadystatechange = function(){
      if(xhr.readyState === XMLHttpRequest.DONE){
        var serverAnswer = JSON.parse(xhr.response);
        callback(serverAnswer);
      }
    };
  }
};

function App() {
  this.ajax = new Ajax();
  this.initLoad = this.ajax.openDatabase(this.listDatabase.bind(this));
  this.addInputHandler();
}

App.prototype = {
  constructor: App,

  parentUl: document.querySelector("#todo-list-ul"),

  inputButton: document.querySelector("button"),

  inputField: document.querySelector("input"),

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
      this.ajax.deleteDatabase(id, function () {
        console.log(this);
        this.ajax.openDatabase(this.listDatabase.bind(this));
      }.bind(this));
    }.bind(this));

    var completedChange = !completed;
    checkButtonDiv.addEventListener("click",function(){
      this.ajax.putDatabase(text, id, completedChange, function () {
        this.ajax.openDatabase(this.listDatabase.bind(this));
      }.bind(this));
    }.bind(this));
  },

  listDatabase: function(serverAnswer) {
    var deleteAll = document.querySelector("#todo-list-ul");
    deleteAll.innerHTML = "";
    serverAnswer.forEach(function(item) {
      this.addTodoItem(item.id, item.text, item.completed);
    }.bind(this));
  },

  addInputHandler: function() {
      this.inputButton.addEventListener("click", function(){
      this.ajax.postDatabase(this.inputField.value, function() {
        this.ajax.openDatabase(app.listDatabase.bind(this));
      }.bind(this));
    }.bind(this));
  }

};
var app = new App();


// ---------------BONUS-BUTTON-ANIM---------------//

var inputButton = document.querySelector("button");

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


//----------------SWITCH-THEME---------------//

var themeArray = ["style_origin.css", "style_handcrafted.css"];
var arrayIndex = 0;
var themeButton = document.querySelector(".theme-button");
var themeCSS = document.querySelector("#theme_css");

function themeChange() {
  if(arrayIndex === 0) {
    arrayIndex = 1;
  } else {
    arrayIndex = 0;
  }
  themeCSS.href = themeArray[arrayIndex];
}

themeButton.addEventListener("click", themeChange);
