import OCRtoText as ott
import utils.constants as ct
import promptGenerator as pg
import speechtotext as sp
import wordParser as wp
import requests
import openai

screenfile = None

def imageGeneration (in_prompt):
  openai.api_key = ct.OPENAI_API_KEY
  response= openai.Image.create(
    prompt=in_prompt,
    n=1,
    size="1024x1024"
  )
  return response

#parses text from display screen for context
def generate_image_from_text(audio_transcript, screen_transcipt, output_file):
  if screen_transcipt != None:
    screenText = ott.imagetotext(screen_transcipt)
  else:
    screenText = None

  with open(audio_transcript, 'r') as audio:
    transcript = audio.read()

  #looks for keywords in the audio signal
  keywords = wp.extract_keywords_plain(transcript)

  #creates the prompt using the keywords from the audio and the context from the display screen
  sentence = pg.promptGenerator(screenText, keywords)

  max_length = 10
  words = sentence.split()[:max_length]
  truncated_sentence = " ".join(words)

  response = imageGeneration(truncated_sentence)
  url = response['data'][0]['url']

  # Send a GET request to the URL and get the content of the response
  response = requests.get(url)
  with open(output_file, "wb") as f:
      f.write(response.content)

import time
import microphone as mc
import speechtotext as sp

if __name__ == '__main__':
  # recorder = mc.Recorder()

  # print('Recording!')
  # recorder.start_recording()
  # time.sleep(5)
  # print('Stopped recording!')
  # recorder.stop_recording('out.wav')

  # sp.get_transcript('out.wav', 'audio.txt')

  generate_image_from_text('audio.txt', None, 'image.png')