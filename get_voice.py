from speech_recognition import *

r = Recognizer()
'''with Microphone() as src:
    r.adjust_for_ambient_noise(src)'''


def Listen(z):
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
