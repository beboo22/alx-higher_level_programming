#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, data) {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const fdata = JSON.parse(data);
  const completedTask = {};

  for (let i = 0; i < fdata.length; ++i) {
    const userId = fdata[i].userId;
    const complted = fdata[i].completed;

    if (complted) {
      if (completedTask[userId]) {
        completedTask[userId]++;
      } else {
        completedTask[userId] = 1;
      }
    }
  }

  console.log(completedTask);
});
