import ollama

response = ollama.chat(model='myllama3', messages=[
    {'role': 'user', 'content': 'What is teh full form of WHO'}
])
print(response['message']['content'])