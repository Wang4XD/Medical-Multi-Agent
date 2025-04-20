import os

import numpy as np
from PIL import Image
from model_loader import ModelLoader
from config import Config

from PIL import Image
import numpy as np
import torch

def process_image(state):
    """Medical image segmentation processing"""
    img = Image.open(state["image_path"])

    if img.mode != "RGB":
        img = img.convert("RGB")

    model = ModelLoader().segmenter
    processor = ModelLoader().processor  # Suppose the processor is also loaded in the ModelLoader

    try:
        inputs = processor(images=img, return_tensors="pt")

        with torch.no_grad():
            outputs = model(**inputs)

        predicted_map = processor.post_process_semantic_segmentation(
            outputs, target_sizes=[img.size[::-1]]  
        )[0].cpu().numpy()  

    except Exception as e:
        raise ValueError(f"图像分割失败：{str(e)}")

    output_path = os.path.join(Config.OUTPUT_DIR, os.path.basename(state["image_path"]))
    save_segmentation_results(predicted_map, output_path)

    state["result"] = {"type": "image", "path": output_path}
    return state


def save_segmentation_results(predicted_map, output_path):
    if np.max(predicted_map) > 1:  
        predicted_map = (predicted_map / np.max(predicted_map)) * 255
    predicted_map = predicted_map.astype(np.uint8)  

    mask_image = Image.fromarray(predicted_map)

    mask_image.save(output_path)
