SYSTEM_ROLE = """
You are a tool that creates and generates success stories of people career's.
The people, in this moment, are students of the "Colegio Villemar El Carmen" school in Bogotá, Colombia.
The students are between 15 and 18 years old, and they speak Spanish and English.
They are finishing their high school studies and are preparing to enter the university.
The students can have different career aspirations.
You will be asked to generate a success story for each student, one by one.
You will be asked to generate text and images.
"""

TODAY_IMAGE_PROMPT = """
Please, generate a non animated and realistic image with the following characteristics:
The name of the student is {name}.
{pronoun} is Colombian.
The gender of the student is {gender}.
{pronoun} is {age} years old.
{pronoun} has a {hair} hair.
The student is wearing a school uniform. The uniform consists of a blue jacket, a white shirt, a red tie and grey {pants_skirt}.
"""

TODAY_BACKGROUND_IMAGE_CHOICES = (
    """
    The student is standing in a classroom.
    In the background, there is a blackboard with the words 'Colegio Villemar El Carmen' written in Spanish.
    """,
    """
    The student is standing in a hall of the school.
    In the background, there is a signboard with the words 'Colegio Villemar El Carmen' written in Spanish.
    """
    # """
    # The student is standing in a basketball court of the school.
    # In the background, there is a Colombian flag.
    # """,
)

TODAY_TEXT_PROMPT = """
Please, generate a text with the following characteristics:
The name of the student is {name}.
The gender of the student is {gender}.
The student is {age} years old.
The student wants to study {career}.
The student is Colombian and studies in the "Colegio Villemar El Carmen" school, in Bogotá, Colombia.
The student is finishing the high school and preparing for the university.
The student has good grades and is very smart.
The student is very excited about studying {career}.
Generate a text with maximum 100 words describing the current status of the student and the expectations of going to the university to study {career}.
"""

SOME_YEARS_IMAGE_PROMPT = """
Generate a non animated and realistic image showing some students in the university studying {career} in the university.
Provide a background according to the career {career}, showing tools and resources related to the career.
"""

SOME_YEARS_IMAGE_PROMPT_2 = """
With the same person generated in the previous image, please, generate a realistic image showing to {name}:
Do not show the face of the person. Show very little.
The name of the person is {name}.
The person is Colombian.
The gender of the person is {gender}.
The person is {age} years old.
The person has a {hair} hair.
The person is studying {career} in the university and is in the last semesters.
The student is standing in a classroom of the university. Show the person far away in a classroom or in the university campus with other people.
Provide a background according to the career {career}, showing tools and resources related to the career.
"""

SOME_YEARS_TEXT_PROMPT = """
Please, generate a text with the following characteristics:
The name of the person is {name}.
The person is {age} years old.
The person is studying {career} in the university and is in the last semesters.
Generate a story with maximum 100 words describing the current status of the person, describing the achievements and the difficulties of studying {career} in the university.
"""

MANY_YEARS_IMAGE_PROMPT = """
Generate a non animated and realistic image showing people working as a professionals of {career}.
"""

MANY_YEARS_IMAGE_PROMPT_2 = """
With the same person generated in the previous image, please, generate a realistic image showing to {name}:
Do not show the face of the person. Show very little.
The name of the person is {name}.
The person is Colombian.
The gender of the person is {gender}.
The person is {age} years old.
The person has a {hair} hair.
The person finished to study {career} 10 years ago and is a successful worker with many years of experience.
Show the person far away in a place related to the career of {career}, sharing with other people or alone.
Provide a background according to the current status of the person regarding the career {career}.
"""

MANY_YEARS_TEXT_PROMPT = """
Please, generate a text with the following characteristics:
The name of the person is {name}.
The person is {age} years old.
The person finished to study {career} 10 years ago and is a successful worker with many years of experience.
Generate a story with maximum 100 words describing the current status, describing the achievements and the difficulties of working as a professional in {career}.
"""

TRANSLATE_TEXT_PROMPT = """
Please, translate the following text to Spanish: {text}
"""