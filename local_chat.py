import requests
import json

def chat_with_ollama(prompt, model="myllama3"):
    """
    Send a prompt to Ollama and get a response
    
    Args:
        prompt (str): The message to send to the model
        model (str): The name of the model (default: myllama3)
    
    Returns:
        str: The model's response
    """
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "No response received")
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure Ollama is running."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def main():
    print("Ollama Chat Interface")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Get response from Ollama
        print("\nAssistant: ", end="", flush=True)
        response = chat_with_ollama(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()