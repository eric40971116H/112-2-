import time
import pyttsx3

engine = pyttsx3.init()

def make_audio(text , rate =100 , volume=1 ):
    id =int(time.time())
    engine.setProperty("volume",volume)
    engine.setProperty("rate",rate)

    engine.save_to_file(text , "audios/{}.mp3".format(id))
    engine.runAndWait()
    return id