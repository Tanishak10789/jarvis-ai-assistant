import ollama

def aiProcess(command):
    response = ollama.chat(
        model="llama2",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    return response['message']  # Ollama's response format

# Test it
output = aiProcess("What is force")
print(output)
