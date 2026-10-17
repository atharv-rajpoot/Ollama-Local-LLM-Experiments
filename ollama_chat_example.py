from ollama import chat

response = chat(
    model = 'llama3.2',
    messages=[{
        "role":"user",
        "content":"Explain AI in one sentence"
    }]
    )

print(response["message"]["content"])