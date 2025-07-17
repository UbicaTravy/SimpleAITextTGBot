from openai import OpenAI
from config import DEEPSEEK_API_KEY

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

class DeepSeekAnalyzer:
    @staticmethod
    def analyze_text(text: str, model: str = "deepseek-chat") -> str:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Ты полезный ассистент, который анализирует текст"},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            stream=False
        )
        return response.choices[0].message.content
