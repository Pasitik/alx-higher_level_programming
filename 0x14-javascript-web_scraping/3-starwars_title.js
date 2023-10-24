#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const resJson = JSON.parse(body);
    console.log(resJson.title);
  } else {
    console.log('error code: ' + res.statusCode);
  }
});
