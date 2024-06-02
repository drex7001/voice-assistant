from dotenv import load_dotenv
import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load environment variables
load_dotenv()

# Initialize the model and tokenizer
model_name = "Ollama/llama-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def query_llama(query):
    # Tokenize the input query
    inputs = tokenizer(query, return_tensors="pt")
    
    # Generate a response
    with torch.no_grad():
        outputs = model.generate(inputs.input_ids, max_length=100, num_return_sequences=1)
    
    # Decode the output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Get user input and query the model
prompt = input("USER: ")
response = query_llama(prompt)
print(f"AI: {response}")