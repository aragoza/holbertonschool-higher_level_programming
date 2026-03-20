#!/usr/bin/node
function factorial (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const args = process.argv;
if (args[2]) {
  console.log(factorial(args[2]));
} else {
  console.log(factorial(1));
}
