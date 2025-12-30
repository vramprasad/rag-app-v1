import requests
try:
    print(requests.get("http://127.0.0.1:11434").text)
except Exception as e:
    print(f"Direct connection failed: {e}")    
    