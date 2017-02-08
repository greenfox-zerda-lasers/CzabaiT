const array = [0, 2, 4, 6, 8, 10, 12, 46, 78, 90, 144];
const searchedValue = 142;

function binarySearch () {
  let low = 0;
  let high = array.length - 1;

  while(true) {
    if (low > high) {
      return false;
    } else {
      let mid = Math.round(( low + high ) / 2);
      if (array[mid] > searchedValue) {
        high = mid - 1;
      } else if (array[mid] < searchedValue) {
        low = mid + 1;
      } else if (array[mid] === searchedValue) {
        return true;
      }
    }
  }
}

console.log(binarySearch());
