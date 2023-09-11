#!/usr/bin/node

let i = parseInt(process.argv[2]);

if (isNaN(i) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (; i > 0; i--) {
    console.log('C is fun');
  }
}
