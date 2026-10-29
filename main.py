python
import os
import requests
from groq import Groq

# المفاتيح من Secrets
PAGE_ID = os.getenv("PAGE_ID")
FB_TOKEN = os.getenv("FB_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_post():
    client = Groq(api_key=GROQ_API_KEY)
    prompt = """
    كتب بوست قصير وجذاب لصفحة فيسبوك حول الذكاء الاصطناعي.
    يكون مفيد، تحفيزي، وبالدارجة المغربية أو العربية الفصحى البسيطة.
    مع هاشتاغات. لا يتجاوز 3 أسطر.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return completion.choices[0].message.content.strip()

def post_to_facebook(message):
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    data = {
        "message": message,
        "access_token": FB_TOKEN
    }
    r = requests.post(url, data=data)
    print(r.text)
    if r.status_code == 200:
        print("✅ تم النشر بنجاح!")
    else:
        print("❌ فشل النشر")

if __name__ == "__main__":
    post_text = generate_post()
    print(f"البوست: {post_text}")
    post_to_facebook(post_text)
    
