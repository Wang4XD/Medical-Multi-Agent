import os

import numpy as np
from PIL import Image
from model_loader import ModelLoader
from config import Config

from PIL import Image
import numpy as np
import torch

def process_image(state):
    """医学图像分割处理"""
    img = Image.open(state["image_path"])

    # 确保图像为 RGB 格式
    if img.mode != "RGB":
        img = img.convert("RGB")

    # 加载模型
    model = ModelLoader().segmenter
    processor = ModelLoader().processor  # 假设 ModelLoader 中也加载了 processor

    # 调用模型进行分割
    try:
        # 准备输入
        inputs = processor(images=img, return_tensors="pt")

        # 执行推理
        with torch.no_grad():
            outputs = model(**inputs)

        # 后处理分割结果
        predicted_map = processor.post_process_semantic_segmentation(
            outputs, target_sizes=[img.size[::-1]]  # 目标尺寸为原始图像尺寸
        )[0].cpu().numpy()  # 获取分割结果并转换为 NumPy 数组

    except Exception as e:
        raise ValueError(f"图像分割失败：{str(e)}")

    # 将分割结果保存为图像
    output_path = os.path.join(Config.OUTPUT_DIR, os.path.basename(state["image_path"]))
    save_segmentation_results(predicted_map, output_path)

    state["result"] = {"type": "image", "path": output_path}
    return state


def save_segmentation_results(predicted_map, output_path):
    """保存分割结果"""
    # 将分割结果归一化到 0-255 范围
    if np.max(predicted_map) > 1:  # 如果掩码值大于 1，则归一化
        predicted_map = (predicted_map / np.max(predicted_map)) * 255
    predicted_map = predicted_map.astype(np.uint8)  # 转换为 uint8 类型

    # 将分割结果转换为 PIL 图像
    mask_image = Image.fromarray(predicted_map)

    # 保存图像
    mask_image.save(output_path)