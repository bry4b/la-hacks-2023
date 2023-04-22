import utils.constants as ct
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

import openai
import microphone 

openai.api_key = ct.OPENAI_API_KEY

def get_transcript(image=False) -> str:
    key = 'v' if image else 'space'
    filename = microphone.get_user_recording(key)
    with open(filename, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
    os.remove(filename)
    return transcript

def get_image_prompt() -> str:
    return get_transcript(image=True)

def get_bullet_prompt() -> str:
    return get_transcript(image=False)