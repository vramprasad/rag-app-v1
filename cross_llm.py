import requests
import json

url = "http://localhost:11435/api/generate"

payload = {
    "model": "myllama3",
    "prompt": "What is the capital of India? "
}

response = requests.post(url, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        print(data.get("response", ""), end="", flush=True)
