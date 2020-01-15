from gtts import gTTS
import os
from reddit import generate_text

def generate_audio():
    text_title = generate_text()
    text = text_title["text"]
    title = text_title["title"]
    language = "en"
    print("Generating Speech")
    output = gTTS(text = text, lang = language, slow = False)
    print("Saving in file")
    audio_file_name = "op.mp3"
    output.save(audio_file_name)
    print("Audio Generated")
    return {"audio": audio_file_name, "title": title}