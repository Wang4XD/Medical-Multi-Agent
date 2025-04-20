import os
import streamlit as st
from workflow import create_workflow
from file_utils import save_uploaded_file

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)
def main():
    st.title("Medical AI Agent")

    user_input = st.text_input("输入您的问题或指令：")
    uploaded_file = st.file_uploader("上传医学图片（可选）", type=["png", "jpg", "jpeg"])

    if uploaded_file or user_input:
        state = {
            "user_input": user_input,
            "image_path": "",
            "task_type": "",
            "result": None
        }

        if uploaded_file:
            state["image_path"] = save_uploaded_file(uploaded_file)

        workflow = create_workflow().compile()
        final_state = workflow.invoke(state)

        if final_state["result"]["type"] == "image":
            st.success(f"分割结果已保存至：{final_state['result']['path']}")
            st.image(final_state["result"]["path"])
        else:
            st.markdown(f"**回答**：{final_state['result']['content']}")


if __name__ == "__main__":
    main()
