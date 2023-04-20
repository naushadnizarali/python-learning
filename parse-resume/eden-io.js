const axios = require('axios').default;
const fs = require("fs");
const FormData = require("form-data");

const form = new FormData();
form.append("providers", "affinda");
form.append("file", fs.createReadStream("/Volumes/MobileDev/python-learning/datasets/data/INFORMATION-TECHNOLOGY/10089434.pdf"));

const options = {
  method: 'POST',
  url: 'https://api.edenai.run/v2/ocr/resume_parser',
  headers: {
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzU3ZGM4NjgtNjBlZS00YTBjLTg3YjItZmExNWRmZTVmZmNkIiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.thL36yc6r94LAk_29GUKxw7IqBQIyFHxr_lhdZcZxw4',
    'Content-Type': 'multipart/form-data; boundary=' + form.getBoundary()
  },
  data: form
};

axios
  .request(options)
  .then((response) => {
    console.log(JSON.stringify(response.data));
  })
  .catch((error) => {
    console.error(error);
  });