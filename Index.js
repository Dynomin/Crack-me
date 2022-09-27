// Dependencies to install:
// $ npm install node-fetch --save

const fetch = require('node-fetch');

const options = {
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
    Authorization: 'Bearer pk_prod_40FZMTG8EC42GKM4307J52QG14YM'
  },
  body: JSON.stringify({
    "message": {
      "to": {
        "email": "thorvaibhav2020@gmail.com"
      },
      "content": {
        "title": "Trial",
        "body": "Hello there"
      }
    }
  })
};

fetch('https://api.courier.com/send', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));