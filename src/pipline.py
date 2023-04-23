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
def generate_image_from_text(transcript, output_file, screen_transcript=False, mood=None):
  if screen_transcript:
    screenText = ott.imagetotext(transcript)
  else:
    screenText = None

  # with open(transcript, 'rb') as audio:
  #   transcript_read = audio.read()
  transcript_read = sp.get_transcript(transcript, 'transcript.txt')

  #looks for keywords in the audio signal
  #keywords = wp.extract_keywords_plain(transcript)

  #creates the prompt using the keywords from the audio and the context from the display screen
  sentence = pg.promptGenerator(screenText, transcript_read, mood)

  response = imageGeneration(sentence)
  url = response['data'][0]['url']

  # Send a GET request to the URL and get the content of the response
  response = requests.get(url)
  with open(output_file, "wb") as f:
      f.write(response.content)

import time
import microphone as mc
import speechtotext as sp

if __name__ == '__main__':
  recorder = mc.Recorder()

  print('Recording!')
  recorder.start_recording()
  time.sleep(5)
  print('Stopped recording!')
  recorder.stop_recording('out.wav')

  sp.get_transcript('out.wav', 'audio.txt')

  generate_image_from_text('audio.txt', 'image.png')