import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_DIR = r"C:\Users\Administrator\Desktop\agent\model"
    UPLOAD_DIR = "uploads"
    OUTPUT_DIR = "outputs"