from model_loader import ModelLoader
from config import Config


class MultimodalQA:
    def __init__(self):
        self.bot = ModelLoader().huatuo_vision_bot

    def answer_question(self, state):
        """Multimodal analysis and question-answering processing"""
        query = state["user_input"]
        image_paths = [state["image_path"]] if state.get("image_path") else []

        try:
            output = self.bot.inference(query, image_paths)
            state["result"] = {"type": "text", "content": output}
        except Exception as e:
            state["result"] = {"type": "text", "content": f"多模态问答失败：{str(e)}"}

        return state
