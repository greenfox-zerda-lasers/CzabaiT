var romanDict = {
  1: 'I',
  5: 'V',
  10: 'X',
  50: 'L',
  100: 'C',
  500: 'D',
  1000: 'M'
};

var dividerList = [1000, 500, 100, 50, 10, 5, 1];

var converter = {

  float2string: function(num) {
    return num.toString();
  },

  string2float: function(str) {
    return parseFloat(str);
  },

  int2roman: function(number) {
    var romanString = '';
    var multiplier = 0;
    for(var value of dividerList) {
      console.log(value);
      multiplier = number % value;
      while (multiplier > 0) {
        romanString += romanDict[value];
        multiplier--;
      }
    }
    return romanString;
  },

  roman2int: function(number) {}
};

console.log(converter.float2string(345),typeof(converter.float2string(345)));
console.log(converter.string2float('8347'),typeof(converter.string2float('8347')));
console.log(converter.int2roman(1347),typeof(converter.int2roman(1347)));
