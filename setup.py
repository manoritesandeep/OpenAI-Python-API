import openai
import os

# Setup key: os.environ["NAME"] = "PASTE_KEY_HERE"
# 
# To get string of the key
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = 'Give me two reasons to learn OpenAI API with python',
    max_tokens = 300
)
# print(response)
print(response['choices'][0]['text'])

