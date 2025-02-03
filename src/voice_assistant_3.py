import openai

openai.api_key = ""  # Replace with your API key

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a helpful AI assistant."},
                  {"role": "user", "content": prompt}]
    )
    reply = response["choices"][0]["message"]["content"]
    print(f"🤖 AI Response: {reply}")
    return reply

# Test AI response
if __name__ == "__main__":
    text = recognize_speech()
    if text:
        translated_text = translate_text(text, "en")  # Translate to English
        ai_reply = get_ai_response(translated_text)
