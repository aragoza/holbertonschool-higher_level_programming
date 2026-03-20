#!/usr/bin/node
const args = process.argv;
if (parseInt(args[2])) {
  let i = 0;
  while (i < parseInt(args[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
