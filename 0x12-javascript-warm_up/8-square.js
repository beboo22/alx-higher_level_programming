#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    const row = 'X'.repeat(size);
    console.log(row);
  }
}
