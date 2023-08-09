import os
import openai

openai.api_key = "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"
prompt = "Hello"
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
    {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message)