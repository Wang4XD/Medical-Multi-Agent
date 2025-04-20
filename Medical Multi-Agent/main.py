import os
import streamlit as st
from workflow import create_workflow
from file_utils import save_uploaded_file

# 初始化目录
os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
def main():
    st.title("Medical AI Agent")

    # 用户输入
    user_input = st.text_input("输入您的问题或指令：")
    uploaded_file = st.file_uploader("上传医学图片（可选）", type=["png", "jpg", "jpeg"])

    if uploaded_file or user_input:
        # 初始状态
        state = {
            "user_input": user_input,
            "image_path": "",
            "task_type": "",
            "result": None
        }

        # 保存上传文件
        if uploaded_file:
            state["image_path"] = save_uploaded_file(uploaded_file)

        # 执行工作流
        workflow = create_workflow().compile()
        final_state = workflow.invoke(state)

        # 显示结果
        if final_state["result"]["type"] == "image":
            st.success(f"分割结果已保存至：{final_state['result']['path']}")
            st.image(final_state["result"]["path"])
        else:
            st.markdown(f"**回答**：{final_state['result']['content']}")


if __name__ == "__main__":
    main()