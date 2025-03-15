from gtts import gTTS
import os


# Automatically convert the initial text to speech and play it for the user
text = "Hello! I am a text-to-speech program. Would you like to give me a try? Be creative!"
language, tld = "en", "ca"
speech = gTTS(text=text, lang=language, tld=tld, slow=False)
speech.save("greeting.mp3")
os.system("greeting.mp3")

# Continue asking the user for input and converting it to speech
while True:
    user_text = input(
        "\nThe AI revolution is here! What message do you want to send to humanity? "
        "(Type your text or 'exit' to quit): \n"
    )
    if user_text.lower() == "exit":
        print("Goodbye!")
        break

    speech = gTTS(text=user_text, lang=language, slow=False)
    speech.save("text-to-speech.mp3")
    os.system("text-to-speech.mp3")
