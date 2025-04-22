# Medical-Multi-Agent
A Medical Multi-Agent System. Using GPT-4o as the brain, the pre-trained model on huggingface (https://huggingface.co/) is invoked for downstream task processing.


Thank the following authors:

https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B

https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B

https://huggingface.co/wanglab/medsam-vit-base

https://huggingface.co/facebook/mask2former-swin-large-cityscapes-semantic


## Processing Flow

1. User input → 2. GPT-4o Intent recognition → 3. Route decision → 4. Execute the corresponding Agent → 5. Return the result


## Project Structure

```
├── Agent
    ├── model
        ├── HuatuoGPT-o1-7B
        ├── ...
        ├── ...
    ├── medical_multi_Agent
        ├── llava
        ├── uploads
        ├── main.py
        ├── workflow.py
        ├── ...
        ├── ...
    ├── .env
``` 


## Quick Start

1. Create the .env file and complete the configuration of API_KEY and URL

2. Download the corresponding weight file into the model folder

3. ```python main.py```
