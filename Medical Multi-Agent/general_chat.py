from openai import OpenAI
from config import Config


def general_chat(state):
    """General question Answers"""
    client = OpenAI(api_key=" ")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是一个友好的助手，可以回答用户的提问。"},
            {"role": "user", "content": state["user_input"]}
        ]
    )

    state["result"] = {"type": "text", "content": response.choices[0].message.content}
    return state
