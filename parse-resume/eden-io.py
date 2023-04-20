import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzU3ZGM4NjgtNjBlZS00YTBjLTg3YjItZmExNWRmZTVmZmNkIiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.thL36yc6r94LAk_29GUKxw7IqBQIyFHxr_lhdZcZxw4"}

url="https://api.edenai.run/v2/ocr/resume_parser"
data={"providers": "affinda"}
files = {'file': open("/Volumes/MobileDev/python-learning/datasets/data/INFORMATION-TECHNOLOGY/10265057.pdf",'rb')}

response = requests.post(url, data=data, files=files, headers=headers)

result = json.loads(response.text)
print(result['affinda']['extracted_data'])
