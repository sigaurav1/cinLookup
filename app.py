import requests
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Item(BaseModel):
    companyName: str

@app.post('/companySearch')
def companySearch(item:Item):
    if item.companyName:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
        }
        url = f'https://mca.gov.in/mcafoportal/cinLookup.do?companyname={item.companyName}'
        response = requests.get(url=url, headers= headers)
        print(response.text)
        return json.loads(response.text)