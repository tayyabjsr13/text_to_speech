import pyttsx3
import os

def text_to_speech():
    engine = pyttsx3.init()
    # filename = os.path.join('data', 'data_1.txt')
    filename = os.path.join('data', 'data_2.txt')



    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', 'f5')
    # engine.setProperty('voice', 'm6s')
    # engine.setProperty('voice', 'en+m3')
    # for voice in voices:
    #     print(f"{voice.id} {voice.name} {voice.languages} {voice.gender} {voice.age}")
        # break

    # print(f"{voices}")

    # volume = engine.getProperty('volume')
    # print(f"{volume}")

    # rate = engine.getProperty('rate')
    # print(f"{rate}")
    # engine.setProperty('rate', 190)





    with open(filename) as rf:
        for line in rf:
            print(line)
            engine.say(line)
            engine.runAndWait()

if __name__ == '__main__':
    text_to_speech()