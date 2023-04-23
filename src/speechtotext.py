import utils.constants as ct
import os
import threading

import openai
from flask import Flask, redirect, render_template, request, url_for

import openai
import microphone 

openai.api_key = ct.OPENAI_API_KEY

def get_transcript(input_file, output_file=None, bullet=False) -> None:
    with open(input_file, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
    os.remove(input_file)
    if bullet:
        print(transcript)
        return transcript
    else:
        with open(output_file, 'w') as f:
            f.write(transcript)
    return transcript