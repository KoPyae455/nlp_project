import openai

openai.api_key = "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"  # Replace with your API key

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
