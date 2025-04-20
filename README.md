# Medical-Multi-Agent
Medical Multi-Agent. Using GPT-4o as the brain, the pre-trained model on huggingface (https://huggingface.co/) is invoked for downstream task processing.

Thank the following authors:
https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B
https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B
https://huggingface.co/wanglab/medsam-vit-base

Process: 1. User input → 2. GPT-4o Intent recognition → 3. Route decision (pipeline) → 4. Execute the corresponding Agent → 5. Return the result
