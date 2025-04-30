import json
import requests
import utilities
from dotenv import load_dotenv
import os

load_dotenv()
var_a = os.getenv("VAR_A")
var_b = os.getenv("VAR_B")

print(var_a)
print(var_b)

def lambda_handler(event,context):
    url = "www.google.com"
    
    print("fetching url !")
    resp = requests.get(url)
    with open("/tmp/demofile.txt", "a") as f:
        f.write("Now the file has more content!")
        
    if resp.status_code == 200:
        return {'status-code' : 200,
                'body' : utilities.add(var_b,var_a)}