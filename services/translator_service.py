import openai
from configurations import config
import requests
from configurations.config import OPENAI_API_KEY,MIXTRAL_API_KEY,MIXTRAL_API_URL,GEMINI_API_KEY
import google.generativeai as genai
genai.configure(api_key=GEMINI_API_KEY)

openai.api_key = config.OPENAI_API_KEY

def translate_text(text, target_language,model):
    prompt = f"Translate the following text to {target_language}:\n\n{text}"

    if model=="mixtral":
        headers = {
            "Authorization": f"Bearer {MIXTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b",
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(MIXTRAL_API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"].strip()
    elif model=="gemini":
        model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
        response = model.generate_content(prompt)
        return response.text
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response['choices'][0]['message']['content'].strip()
