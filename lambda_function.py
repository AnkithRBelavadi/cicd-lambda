import json
import requests
import utilities

def lambda_handler(event,context):
    url = "www.google.com"
    
    print("fetching url !")
    resp = requests.get(url)
    with open("/tmp/demofile.txt", "a") as f:
        f.write("Now the file has more content!")
        
    if resp.status_code == 200:
        return {'status-code' : 200,
                'body' : utilities.add(4,5)}