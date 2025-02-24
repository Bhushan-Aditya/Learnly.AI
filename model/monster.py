from typing import TypedDict
from utils import getenv
from openai import OpenAI

#BHEN KE LODE CALL UTHA

client = OpenAI(
    base_url="https://llm.monsterapi.ai/v1/",
    api_key=getenv('MONSTER_KEY')
)

model_name = "google/gemma-2-9b-it"

class PromptOptions(TypedDict):
    system: str
    user: str

def monster_generate(opts: PromptOptions) -> str:
    # Format the messages based on the PromptOptions
    messages = [
        {"role": "system", "content": opts["system"]},
        {"role": "user", "content": opts["user"]}
    ]

    completion = client.chat.completions.create(
        model=model_name,  # Use the model_name variable
        messages=messages,  # Use the formatted messages
        temperature=0.9,
        top_p=0.9,
        max_tokens=1000,
        stream=True
    )

    # Handle streaming response
    full_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            full_response += chunk.choices[0].delta.content

    return full_response.strip()
