import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio, language="th-TH")  # Default: Thai
        print(f"🗣 Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("🤖 Could not understand audio.")
        return None
    except sr.RequestError:
        print("🚨 API error.")
        return None

# Test the speech recognition
if __name__ == "__main__":
    recognize_speech()


