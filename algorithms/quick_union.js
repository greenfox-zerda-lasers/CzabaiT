function QuickUnion (arrayLen) {
  this.arrayLen = arrayLen;
  this.array = (function(len) {
    let array = [];
    for (let i = 0; i < len; i++) {
      array.push(i);
    }
    return array;
  })(this.arrayLen);

  this.unite = function () {

  };
};

const quick = new QuickUnion (6);
console.log(quick.array);
