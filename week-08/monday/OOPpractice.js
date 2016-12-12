function Question(theQuestion, theChoices, theCorrectAnswer) {
  this.question = theQuestion;
  this.choices = theChoices;
  this.correctAnswer = theCorrectAnswer;
  this.userAnswer = "";

  var newDate = new Date();
  QUIZ_CREATED_DATE = newDate.toLocaleDateString();
  this.getQuizDate = function() {
    return QUIZ_CREATED_DATE;
  };

  console.log("Quiz Created On: " + this.getQuizDate());
}

Question.prototype.getCorrectAnswer = function() {

};


question = new Question("Na?", ["Yes", "No", "Maybe"], "Yes");
question.getQuizDate();
