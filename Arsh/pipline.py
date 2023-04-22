import OCRtoText as ott
import constants as ct
import promptGenerator as pg
import wordParser as wp
import testingDalle as td
import requests
import os
import openai

prompt = "native americans"
screenfile = "historyClass.png"

def imageGeneration (in_prompt):
  openai.api_key = ct.OPENAI_API_KEY
  response= openai.Image.create(
    prompt=in_prompt,
    n=1,
    size="1024x1024"
  )
  return response

#parses text from display screen for context
def backendPipeline(voicemsg, screenfile):
    screenText = ott.imagetotext(screenfile)
    print(screenText)

    #looks for keywords in the audio signal
    keywords = wp.extract_keywords_plain(voicemsg)

    #creates the prompt using the keywords from the audio and the context from the display screen
    sentence = pg.promptGenerator(screenText, keywords)
    max_length = 10

    words = sentence.split()[:max_length]
    truncated_sentence = " ".join(words)

    print(truncated_sentence)

    response = imageGeneration(truncated_sentence)
    print(response)
    url = response['data'][0]['url']

    # Send a GET request to the URL and get the content of the response
    response = requests.get(url)
    with open("test.png", "wb") as f:
        f.write(response.content)


backendPipeline(prompt, screenfile)