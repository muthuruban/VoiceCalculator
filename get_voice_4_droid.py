# from plyer import stt      #NOT_WORKING_PROPERLY
from speech_recognition import *
from plyer import audio
from kivy.utils import platform
from speech_recognition import *

result = str()
error_code = []

# Refer it in
"""
https://www.google.com/search?client=firefox-b-d&q=plyer.stt+in+python
"""
"""
https://stackoverflow.com/questions/62236419/how-to-use-speech-to-text-in-plyer-its-not-working
"""


def speech(state=None):
    if (platform == 'android'):
        if state == 0:
            audio.start()
            return "Listening..."
        elif state == 1:
            audio.stop()
            aud_path = audio.file_path
            print(aud_path)
            r = Recognizer()
            with WavFile(aud_path) as source:
                audio_record = r.record(source)
            try:
                given = r.recognize_google(audio_record)
                return given
            except IOError:
                return "Sorry no microphone detected."
            except RequestError:
                return "Sorry! couldn't reach the server,check your internet connection and try again."
            except UnknownValueError:
                return "Sorry! can't get your words,try again."
    else:
        r = Recognizer()
        with Microphone() as source:
            audio = r.listen(source, 10, 7)
        try:
            given = r.recognize_google(audio, language='en')
            return given.lower()
        except IOError:
            return "Sorry no microphone detected."
        except RequestError:
            return "Sorry! couldn't reach the server,check your internet connection and try again."
        except UnknownValueError:
            return "Sorry! can't get your words,try again."

