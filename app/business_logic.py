import logging
from typing import Tuple

import random

from app import prompts
from app.api_logic import get_completion_image, get_completion_text
from app.models import Student
from app.utils import store_image


logger = logging.getLogger('Career AI')


async def generate_today_text(student: Student) -> Tuple[str, str]:
    prompt = prompts.TODAY_TEXT_PROMPT.format(
        name=student.name,
        gender=student.gender,
        age=student.age,
        career=student.career,
    )

    text = await get_completion_text(prompt)

    logger.info(f'Generated Today Text Successfully')

    translated_text = await translate_text(text)

    return text, translated_text


async def generate_today_image(student: Student) -> str:
    prompt = prompts.TODAY_IMAGE_PROMPT.format(
        name=student.name,
        age=student.age,
        gender=student.gender,
        hair=student.hair,
        pronoun='he' if student.gender == 'MALE' else 'she',
        pants_skirt='pants' if student.gender == 'MALE' else 'skirt',
    )

    if student.glasses:
        prompt += 'The student wears glasses.'

    background, *_ = random.choices(prompts.TODAY_BACKGROUND_IMAGE_CHOICES)
    prompt += background

    image_url = await get_completion_image(prompt)
    local_image_path = store_image(image_url)

    logger.info(f'Generated Today Image Successfully')

    return local_image_path


async def generate_some_years_text(student: Student) -> Tuple[str, str]:
    prompt = prompts.SOME_YEARS_TEXT_PROMPT.format(
        name=student.name,
        gender=student.gender,
        age=student.age + 5,
        career=student.career,
    )

    text = await get_completion_text(prompt, temperature=0.7)

    logger.info(f'Generated Some Years Text Successfully')

    translated_text = await translate_text(text)

    return text, translated_text


async def generate_some_years_image(student: Student) -> str:
    prompt = prompts.SOME_YEARS_IMAGE_PROMPT_2.format(
        name=student.name,
        age=student.age + 5,
        gender=student.gender,
        hair=student.hair,
        career=student.career,
    )
    if student.glasses:
        prompt += 'The person wears glasses.'

    image_url = await get_completion_image(prompt)
    local_image_path = store_image(image_url)

    logger.info(f'Generated Some Years Image Successfully')

    return local_image_path


async def generate_many_years_text(student: Student) -> Tuple[str, str]:
    prompt = prompts.MANY_YEARS_TEXT_PROMPT.format(
        name=student.name,
        gender=student.gender,
        age=student.age + 15,
        career=student.career,
    )

    text = await get_completion_text(prompt, temperature=0.8)

    logger.info(f'Generated Many Years Text Successfully')

    translated_text = await translate_text(text)

    return text, translated_text


async def generate_many_years_image(student: Student) -> str:
    prompt = prompts.MANY_YEARS_IMAGE_PROMPT_2.format(
        name=student.name,
        age=student.age + 15,
        gender=student.gender,
        hair=student.hair,
        career=student.career,
    )

    if student.glasses:
        prompt += 'The person wears glasses.'

    image_url = await get_completion_image(prompt)
    local_image_path = store_image(image_url)

    logger.info(f'Generated Many Years Image Successfully')

    return local_image_path


async def translate_text(input_text: str) -> str:
    prompt = prompts.TRANSLATE_TEXT_PROMPT.format(
        text=input_text,
    )

    text = await get_completion_text(prompt, temperature=0.2)

    logger.info(f'Translated text to Spanish successfully')

    return text
