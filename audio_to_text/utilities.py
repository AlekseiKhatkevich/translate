import speech_recognition as sr
import pocketsphinx
import os
from translate.settings import MEDIA_ROOT
from googletrans import Translator


def get_text_from_audio(filename, duration):
    """Function extracts text from audio"""
    r = sr.Recognizer()
    file = sr.AudioFile((os.path.join(MEDIA_ROOT, "file_storage", filename)))
    with file as source:
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


if __name__ == "__main__":

    a = translate_lng_lo_lng("this episode is brought you by square square is more than a little white credit card reader it's a run your whole Business System including point-of-sale payroll invoices access to business loans and more it's all built to work together learn House Square can help run and grow your business at square.com start up with another episode of without fail was up for one of the most anticipated Awards of the evening best new restaurant" , dest="ru")

    print(a)
