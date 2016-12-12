var valtozo;

var lista = {
  "valtozo": 45,
  "fuggveny": function() {
    return "ez mar fuggveny";
  },
  "fuggveny2": function() {
    return this.valtozo + 55;
  }
};

for (var key in lista) {
  if (typeof(lista[key]) === "function" && key === "fuggveny2") {
  console.log(lista[key]());}
}

/*lista.forEach(function(elem) {
  if (typeof(lista[key]) === "function") {
  console.log(lista[key]());}
});*/
