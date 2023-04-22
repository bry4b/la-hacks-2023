import microphone.constants as constants
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

import openai
import microphone 

openai.api_key = constants.OPENAI_API_KEY

filename = microphone.get_user_recording()
with open(filename, "rb") as audio_file:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
print(transcript)
os.remove(filename)