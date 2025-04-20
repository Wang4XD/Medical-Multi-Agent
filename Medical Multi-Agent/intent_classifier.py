from openai import OpenAI
import json
from config import Config


def intent_classifier(state):
    """Use GPT-4o for intent classification. The prompt content can be further expanded based on the task"""
    client = OpenAI(api_key="YOUR_API_KEY")

    prompt = f"""
    请分析用户请求类型：
    用户输入：{state["user_input"]}
    用JSON格式返回，包含task_type字段，task_type即有且只有一个
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    result = json.loads(response.choices[0].message.content)
    print("GPT Result：")
    print(result)
    state["task_type"] = result["task_type"]
    return state
