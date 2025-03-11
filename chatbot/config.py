import os
from openai import OpenAI

import dotenv

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)



def chat(messages):
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=messages,
    )
    answer = completion.choices[0].message.content
    return answer

if __name__ == "__main__":
    chat("how are you?")