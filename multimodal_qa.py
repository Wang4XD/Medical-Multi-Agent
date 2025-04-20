from model_loader import ModelLoader
from config import Config


class MultimodalQA:
    def __init__(self):
        # 加载 HuatuoGPT-Vision 模型
        self.bot = ModelLoader().huatuo_vision_bot

    def answer_question(self, state):
        """多模态问答处理"""
        query = state["user_input"]
        image_paths = [state["image_path"]] if state.get("image_path") else []

        # 调用模型生成回答
        try:
            output = self.bot.inference(query, image_paths)
            state["result"] = {"type": "text", "content": output}
        except Exception as e:
            state["result"] = {"type": "text", "content": f"多模态问答失败：{str(e)}"}

        return state