import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import pyautogui

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return ""

def execute_command(command):
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "increase volume" in command:
        speak("Increasing the volume")
        pyautogui.press("volumeup", presses=5)
    elif "decrease volume" in command:
        speak("Decreasing the volume")
        pyautogui.press("volumedown", presses=5)
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = recognize_speech()
        if command:
            execute_command(command)
