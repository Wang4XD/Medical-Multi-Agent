目标：以GPT-4o为大脑，调用huggingface上的预训练模型进行下游任务处理。

相比较调用tool工具的优点是：适合特定领域的需求。例如需要完成医学图像分割任务，普通Python工具需要手动构建代码实现特征提取、模型训练和评估，耗时且效果可能不如预训练模型。



[requirements.txt](https://www.yuque.com/attachments/yuque/0/2025/txt/34888563/1742952824060-e144a519-0716-46d6-a6bd-45526418d57a.txt)、

项目结构：

![](https://cdn.nlark.com/yuque/0/2025/png/34888563/1742953108359-8aa55985-cfce-435a-b55f-5b86584da559.png)




![](https://cdn.nlark.com/yuque/0/2025/png/34888563/1742954152871-ef8d806c-d0c1-475d-a711-d7aee1e343e5.png)



使用LangGraph、Streamlit构建前后端

https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B

https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B

https://huggingface.co/wanglab/medsam-vit-base

https://huggingface.co/facebook/mask2former-swin-large-cityscapes-semantic（可替换更好的医学分割模型）



流程：1、用户输入 → 2. GPT-4o意图识别 → 3. 路由决策（pipeline） → 4. 执行对应Agent → 5. 返回结果



当识别用户意图为分割时(task_type=image_segmentation)，执行分割pipeline，前后端：

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954189779-6d769171-5059-4010-bdb0-5b9a7c8075f3.jpeg)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954195171-05468458-e999-496c-a1fa-ed84151b03fd.jpeg)

识别用户意图为QA问答时(task_type=medical_qa)，执行思考-回答pipeline，前后端：

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954211608-239e5259-5e3e-4ffd-b2b6-d0e723d23ec2.jpeg)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954217060-590af8f3-f0b5-41c7-b0a2-2df9b254c5d5.jpeg)

识别用户意图问医学图像分析(task_type=multimodal_qa)时，执行图像分析pipeline，前后端：

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954239551-5e47a744-8ba3-43fd-97b0-96f926b97220.jpeg)

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954245301-896d7c69-ee20-4a18-ac91-d573da2eb6a0.jpeg)

-------------------------------------------踩过的坑--------------------------------------------------

报错LlavaQwen2ForCausalLM.forward() got an unexpected keyword argument 'cache_position'

添加cache_position=None

![](https://cdn.nlark.com/yuque/0/2025/jpeg/34888563/1742954342041-3fdcc603-a67f-4705-84cf-1d8792a31bc8.jpeg)



预训练模型配置文件

![](https://cdn.nlark.com/yuque/0/2025/png/34888563/1742954341966-1dc76fe3-d18f-423f-90f4-2c14ed3419d5.png)

![](https://cdn.nlark.com/yuque/0/2025/png/34888563/1742954342426-93be0491-06fb-4532-8c2b-ad687e83a6d8.png)



Exception: data did not match any variant of untagged enum ModelWrapper at line 757443 column 3.

应更新到新版本transformers



ValueError: Unable to create tensor, you should probably activate padding with 'padding=True' to have batched tensors with the same length.

Mask2Former 的 image_processor 需要确保输入图像的尺寸一致，或者启用填充选项。代码已修改



AttributeError: 'list' object has no attribute 'save'.

Mask2Former 模型的分割结果是一个列表（list），而不是可以直接保存的图像对象，应将分割结果转换为图像格式（如 PIL 图像），然后保存为文件。代码已修改



RuntimeError: 视觉编码器未正确加载.

注意工作流中需要添加对应节点，路由决策函数返回的结果应与工作流中的节点名称匹配。代码已修改











----------------------------------------------------后续改进---------------------------------------------------



![](https://cdn.nlark.com/yuque/0/2025/png/34888563/1744266724145-b747301e-f0c8-4250-893f-9d93f8d7885f.png)



















