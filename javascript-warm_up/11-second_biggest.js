#!/usr/bin/node

const args = process.argv;
if (args.length > 2) {
  let i = 2;
  let j = 2;
  while (i < args.length) {
    if (Number(args[j]) < Number(args[i])) {
      j = i;
    }
    i++;
  }
  args.splice(j, 1);
  i = 2;
  let h = Number(args[2]);
  while (i < args.length) {
    if (h < Number(args[i])) {
      h = args[i];
    }
    i++;
  }
  console.log(h);
} else {
  console.log(0);
}
