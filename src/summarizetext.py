import openai
import utils.constants as ct



openai.api_key = ct.OPENAI_API_KEY

def clean_text(transcript):
    transcript = "Clean the following text: \" " + transcript + " \""
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=transcript,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Print the response
    return response.choices[0].text.strip()

def generate_bullet_point(transcript):
    transcript = clean_text(transcript)
    # transcript = "Concisely summarize the following so that it can be used as a review resource for students. " + \
    # "Do not add any new infomation. Use a '-' and return for each bullet point. Do not say anything else. "
    # "You may use nested bullet points. \" " + transcript + " \""
    # transcript = "Using bullet points with a '-', no new information, and proper spacing between each bullet point, write a summary of the "
    # "following: \"" + transcript + "\". " + "tl;dr"
    transcript = transcript + "\ntl:dr and then convert into bullet points."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=transcript,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Print the response
    return response.choices[0].text.strip()

