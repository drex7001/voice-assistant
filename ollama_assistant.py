import ollama

def query_ollama(query):
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': query}
    ])
    return response['message']['content']

prompt = input("USER: ")
response = query_ollama(prompt)
print(f"AI: {response}")