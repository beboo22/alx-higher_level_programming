#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const fs = require('fs');
request(url, function (_err, response, data) {
  fs.writeFile(process.argv[3], data, 'UTF-8', function (_err, response) {

  });
});
