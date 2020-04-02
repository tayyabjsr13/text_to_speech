import pyttsx3
import os


def text_to_speech():
    engine = pyttsx3.init()
    
    # Get current volume
    volume = engine.getProperty('volume')
    
    # Change volume
    # engine.setProperty('volume', volume-0.50)

    
    # Get current speech rate
    rate = engine.getProperty('rate')

    # Change speech rate
    # engine.setProperty('rate', rate-100)

    # Get current voice
    voice = engine.getProperty('voice')

    # Change voice
    engine.setProperty('voice', 'english+f1')
    
    filename = os.path.join('data', 'data_2.txt')

    with open(filename) as rf:
        for line in rf:
            print(line)
            engine.say(line)
            engine.runAndWait()

if __name__ == '__main__':
    text_to_speech()