python
import os
import requests

GROQ_KEY = os.getenv("GROQ_API_KEY")
FB_TOKEN = os.getenv("FB_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

def generate_post():
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{
            "role": "user",
            "content": "كتب ليا بوست قصير جدا (3 أسطر) بالدارجة المغربية + ترجمة بالإنجليزية عن أداة ذكاء صناعي واحدة مفيدة، مع 3 هاشتاغات. خلي الأسلوب مضحك ومشوق كيما أنمي وان بيس. لا تذكر وان بيس كثيرا."
        }],
        "temperature": 0.8
    }
    r = requests.post(url, json=data, headers=headers)
    result = r.json()
    text = result['choices'][0]['message']['content']
    return text

def post_to_facebook(text):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    data = {
        "message": text,
        "access_token": FB_TOKEN
    }
    r = requests.post(url, data=data)
    print("Facebook response:", r.text)
    return r.text

if __name__ == "__main__":
    print("Bot started...")
    post_text = generate_post()
    print("Generated text:", post_text)
    post_to_facebook(post_text)
    print("Done!")
