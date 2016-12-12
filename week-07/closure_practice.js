function makeFunc() {
  var blabla = "Mozilla";
  function displayName() {
    console.log(blabla);
  }
  //displayName();
  return {blabla, displayName};
}

var myFunc = makeFunc();

console.log('MAKEFUNC');
console.log(typeof(makeFunc));
console.log(makeFunc);
console.log(makeFunc.blabla);
console.log(makeFunc());
console.log(makeFunc().displayName());

console.log('\nMYFUNC');
console.log(typeof(myFunc));
console.log(myFunc);
console.log(myFunc.blabla);
console.log(myFunc.displayName());
//console.log(myFunc());
