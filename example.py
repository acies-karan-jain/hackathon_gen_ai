# Assume openai>=1.0.0
from openai import OpenAI
# Create an OpenAI client with your KRUTRIM API KEY and endpoint
  
openai = OpenAI(
    api_key="QSK1tkKG-4edEehUu0S1dAUCuteyaM_w",
    base_url="https://cloud.olakrutrim.com/v1",
)
  
chat_completion = openai.chat.completions.create(
    model="Meta-Llama-3-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hey Tell Me about Acies Global?"}
    ]
)
print(chat_completion.choices[0].message.content)