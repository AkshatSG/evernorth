#For providing the text as context to LLM

#LLM returns our desired data needs

#Still in planning phase

import os
import requests

def generate_answer(context, question, model='distilbert-base-uncased-distilled-squad'): #You can change the model to your needs
    api_key='Your HF API KEY' #Ought to convert this to an env var
    headers={"Authorization": f"Bearer {api_key}"}
    url=f"https://api-inference.huggingface.co/models/{model}"

    payload={
        "inputs": {
            "question": question,
            "context": context
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()
