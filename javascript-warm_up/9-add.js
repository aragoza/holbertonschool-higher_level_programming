#!/usr/bin/node
function add (a, b) {
  const i = a + b;
  console.log(i.toString());
}
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
add(a, b);
