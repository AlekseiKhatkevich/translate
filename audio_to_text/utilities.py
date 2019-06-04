import speech_recognition as sr
import pocketsphinx
import os
from translate.settings import MEDIA_ROOT
from googletrans import Translator
from pydub import AudioSegment
import glob


def get_text_from_audio(filename, duration):
    """Function extracts text from audio"""
    r = sr.Recognizer()
    file = sr.AudioFile(os.path.join(MEDIA_ROOT, "file_storage", filename))
    with file as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.record(source, duration=duration)
    try:
        #result = r.recognize_google(audio)
        result = r.recognize_sphinx(audio)
    except sr.RequestError:
        result = r.recognize_sphinx(audio)
    return result


def translate_lng_lo_lng(text, dest):
    """translates text from english (or other language bu auto-recognition) to a chosen language"""
    translator = Translator()
    translation_result = translator.translate(text, dest=dest).text
    return translation_result








