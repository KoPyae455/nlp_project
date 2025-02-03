from gtts import gTTS
import os

def text_to_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # On Windows, use: os.system("start response.mp3")

# Test Text-to-Speech
if __name__ == "__main__":
    text = recognize_speech()
    if text:
        translated_text = translate_text(text, "en")  # Translate to English
        ai_reply = get_ai_response(translated_text)
        text_to_speech(ai_reply, "en")  # AI speaks response


