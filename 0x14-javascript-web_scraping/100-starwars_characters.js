#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(url, function (_err, response, data) {
  const responseData = JSON.parse(data).characters;
  for (let i = 0; i < responseData.length; ++i) {
    request(responseData[i], function (_cerr, cresponse, cdata) {
      const cresponseData = JSON.parse(cdata);
      console.log(cresponseData.name);
    });
  }
});
