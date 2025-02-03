from googletrans import Translator

def translate_text(text, target_lang="en"):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    print(f"🌍 Translated ({target_lang}): {translated_text.text}")
    return translated_text.text

# Test the translation
if __name__ == "__main__":
    text = recognize_speech()
    if text:
        translate_text(text, "en")  # Translate to English