from openai import AsyncOpenAI
from dotenv import load_dotenv

from app.prompts import SYSTEM_ROLE

load_dotenv()

client = AsyncOpenAI()

GENERAL_MESSAGE = [
    {
        "role": "system",
        "content": SYSTEM_ROLE
    }
]

COMMON_SETTINGS = {
    'max_tokens': 500,
    'top_p': 1,
    'frequency_penalty': 0,
    'presence_penalty': 0,
}


async def get_completion_text(prompt: str, model: str = 'gpt-4-turbo', temperature: float = 0.5) -> str:
    messages = GENERAL_MESSAGE + [
        {
            'role': 'user',
            'content': prompt
        }
    ]

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        **COMMON_SETTINGS,
    )

    return response.choices[0].message.content


async def get_completion_image(prompt: str, model: str = 'dall-e-3') -> str:
    response = await client.images.generate(
        model=model,
        n=1,
        prompt=prompt,
        size='1024x1024',
    )

    return response.data[0].url
