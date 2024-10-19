import os
from dotenv import load_dotenv
import openai

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")

# OpenAI API 키 설정
openai.api_key = api_key

# OpenAI API 호출
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="What is AI?",
    max_tokens=100
)

print(response.choices[0].text.strip())