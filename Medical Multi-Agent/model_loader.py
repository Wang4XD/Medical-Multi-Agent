import logging

from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, AutoImageProcessor, \
    Mask2FormerForUniversalSegmentation, CLIPVisionModel
import torch
from config import Config
from cli import HuatuoChatbot  # HuatuoChatbot is the interface of HuatuoGPT-Vision


class ModelLoader:
    def __init__(self):
        # Image segmentation model
        self.processor = AutoImageProcessor.from_pretrained(r"C:\Users\Administrator\Desktop\agent\model\mask2former")
        self.segmenter = Mask2FormerForUniversalSegmentation.from_pretrained(
            f"{Config.MODEL_DIR}/mask2former",
            offload_folder="./offload" 
        )

        # Medical Question-answering model
        self.medical_llm = AutoModelForCausalLM.from_pretrained(
            f"{Config.MODEL_DIR}/HuatuoGPT-o1-7B",
            device_map="auto",
            torch_dtype=torch.float16,
            offload_folder="./offload"  
        )
        self.medical_tokenizer = AutoTokenizer.from_pretrained(
            f"{Config.MODEL_DIR}/HuatuoGPT-o1-7B",
            device_map="auto",
            torch_dtype=torch.float16,
            offload_folder="./offload"  
        )

        # Medical multimodal model
        self.huatuo_vision_bot = HuatuoChatbot(f"{Config.MODEL_DIR}/HuatuoGPT-Vision-7B")
        print("HuatuoGPT-Vision 模型加载成功！")

