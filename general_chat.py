from openai import OpenAI
from config import Config


def general_chat(state):
    """处理闲聊内容"""
    client = OpenAI(api_key="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")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "你是一个友好的助手，可以回答用户的各种问题。"},
            {"role": "user", "content": state["user_input"]}
        ]
    )

    state["result"] = {"type": "text", "content": response.choices[0].message.content}
    return state