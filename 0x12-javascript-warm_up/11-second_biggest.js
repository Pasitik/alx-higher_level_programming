#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const newArr = [];
  for (const element of process.argv.slice(2)) {
    newArr.push(Number(element));
  }
  console.log(newArr.sort()[newArr.length - 2]);
}
