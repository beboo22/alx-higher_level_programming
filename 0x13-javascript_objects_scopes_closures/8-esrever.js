#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  let indx = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    arr[indx] = list[i];
    indx++;
  }
  return (arr);
};
