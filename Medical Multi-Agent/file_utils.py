import os
from config import Config

def save_uploaded_file(uploaded_file):
    """保存上传文件"""
    save_path = os.path.join(Config.UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path