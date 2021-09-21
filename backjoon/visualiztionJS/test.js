var lastNum = 10;
var sum = 0;

for (let startNum = 1; startNum < lastNum+1; startNum++) {
  setTimeout(function() {
    sum = sum + startNum;
    console.log(startNum)
    console.log("sum: " + sum);
  }, startNum * 1000);
}