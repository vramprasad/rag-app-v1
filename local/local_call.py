import ollama

client = ollama.Client(host='http://localhost:11434')  # Default Ollama port

response = client.chat(model='myllama3', messages=[
    {'role': 'user', 'content': 'What is the full form of WHO'}
])
print(response['message']['content'])