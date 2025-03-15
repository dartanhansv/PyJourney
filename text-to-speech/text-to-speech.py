from gtts import gTTS
import os

text = "Hello, I am a text to speech program. I can convert text to speech in multiple languages."
language = "en"
speech = gTTS(text=text, lang=language, slow=False)
speech.save("speech-from-text.mp3")
os.system("speech-from-text.mp3")
