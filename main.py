import asyncio
import logging

import gradio as gr

from app.models import Student
from app.business_logic import (
    generate_today_text,
    generate_today_image,
    generate_some_years_text,
    generate_some_years_image,
    generate_many_years_text,
    generate_many_years_image,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Career AI')


async def get_resources(student):
    return await asyncio.gather(
        generate_today_text(student),
        generate_today_image(student),
        generate_some_years_text(student),
        generate_some_years_image(student),
        generate_many_years_text(student),
        generate_many_years_image(student),
    )


def generate_story(name, gender, age, hair, glasses, career):
    student = Student(
        name=name,
        gender=gender,
        age=int(age),
        hair=hair,
        glasses=glasses == 'Yes',
        career=career,
    )
    logger.info(f'Student Info Received: {student}')

    loop = asyncio.new_event_loop()
    results = loop.run_until_complete(get_resources(student))

    (
        today_story,
        today_image,
        some_years_story,
        some_years_image,
        many_years_story,
        many_years_image
    ) = results

    english_today_story, spanish_today_story = today_story
    english_some_years_story, spanish_some_years_story = some_years_story
    english_many_years_story, spanish_many_years_story = many_years_story

    story_template = 'ENGLISH:\n\n{english_story}\n\n\n\nSPANISH:\n\n{spanish_story}'

    today_story = story_template.format(
        english_story=english_today_story,
        spanish_story=spanish_today_story,
    )

    some_years_story = story_template.format(
        english_story=english_some_years_story,
        spanish_story=spanish_some_years_story,
    )

    many_years_story = story_template.format(
        english_story=english_many_years_story,
        spanish_story=spanish_many_years_story,
    )

    logger.info('Finished successfully')

    return (
        today_story,
        today_image,
        some_years_story,
        some_years_image,
        many_years_story,
        many_years_image,
    )


with gr.Blocks(
    head='Career AI',
    title="Career AI",
    theme=gr.themes.Monochrome()
) as demo:
    big_block = gr.HTML(
        """
        <h1>Career AI</h1>
        <p>Look your career future!</p>
        """
    )

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Row():
                name_input = gr.Textbox(label="What is your name?")
                age_input = gr.Textbox(label="How old are you?")

            with gr.Row():
                gender_input = gr.Dropdown(
                    choices=["Male", "Female"], label="Gender"
                )
                glasses_input = gr.Dropdown(
                    choices=["Yes", "No"], label="Glasses"
                )

            with gr.Row():
                hair_input = gr.Textbox(label="Hair")

            career_input = gr.Textbox(label="What career would you like to study?")
            submit = gr.Button(value='Submit')

        with gr.Column(scale=3):
            with gr.Tab("You, today:"):
                with gr.Row():
                    image_today = gr.Image(label=None, interactive=False, height=500, width=500)
                    textbox_today = gr.Textbox(label=None, interactive=False, lines=30)

            with gr.Tab("You, in some years:"):
                with gr.Row():
                    image_some_years = gr.Image(label=None, interactive=False, height=500, width=500)
                    textbox_some_years = gr.Textbox(label=None, interactive=False, lines=30)

            with gr.Tab("You, in many years:"):
                with gr.Row():
                    image_many_years = gr.Image(label=None, interactive=False, height=500, width=500)
                    textbox_many_years = gr.Textbox(label=None, interactive=False, lines=30)

        submit.click(
            fn=generate_story,
            inputs=[name_input, gender_input, age_input, hair_input, glasses_input, career_input],
            outputs=[textbox_today, image_today, textbox_some_years, image_some_years, textbox_many_years, image_many_years],
        )


if __name__ == "__main__":
    demo.launch()
