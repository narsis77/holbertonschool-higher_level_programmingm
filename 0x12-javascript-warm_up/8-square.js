#!/usr/bin/node
/*
  js
*/

if (process.argv.length >= 3) {
  const size = process.argv[2];
  if (!isNaN(size)) {
    for (let i = 0; i < parseInt(size); i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
