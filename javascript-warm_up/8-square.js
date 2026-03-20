#!/usr/bin/node
const args = process.argv;
if (parseInt(args[2])) {
  let i = 0;
  while (i < parseInt(args[2])) {
    let j = 0;
    let xnumber = '';
    while (j < parseInt(args[2])) {
      xnumber = xnumber + 'X';
      j++;
    }
    console.log(xnumber);
    i++;
  }
} else {
  console.log('Missing size');
}
