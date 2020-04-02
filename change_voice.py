import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
rate = engine.getProperty('rate')
for voice in voices:
    print(f"voice {voice}")
    engine.setProperty('voice', 'english+f1')
    engine.setProperty('volume', volume+1.5)
    engine.setProperty('rate', rate+50)
    engine.say('The quick brown fox jumped over the lazy dog.')
    break
engine.runAndWait()