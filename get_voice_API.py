from plyer import stt
from speech_recognition import *


class AndroidSTT:
    listening = False
    partial_results = []
    results = []
    errors = []
    str_state = ""

    def __init__(self):
        self.stt = None

    def startListening(self):
        self.stt.start()
        assert self.stt.listening
        self.partial_results = str(self.stt.partial_results)
        self.str_state.join("Listening...")
        return self.str_state

    def stopListening(self):
        try:
            self.stt.stop()
            self.listening = False
            self.results = self.stt.results
            return self.results
        except Exception as e:
            return e


class WindowsSTT:
    r = Recognizer()
    result = ""

    def startListen(self):
        with Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            audio_source = self.r.listen(source)
        try:
            given = self.r.recognize_google(audio_source)
            return str(given.lower())
        except IOError:
            return "Sorry! No input microphone detected."
        except RequestError:
            return "Sorry! can't reach the server, try again later!!"
        except UnknownValueError:
            return "Sorry! can't able to understand, try again!!"
        except WaitTimeoutError:
            return "Waiting timeout"
        except Exception as e:
            return e
