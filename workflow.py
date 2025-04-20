from langgraph.graph import END, StateGraph
from intent_classifier import intent_classifier
from image_segmenter import process_image
from medical_qa import answer_question
from general_chat import general_chat
from multimodal_qa import MultimodalQA

def route_decision(state):
    """路由决策函数"""
    task_type = state["task_type"].lower()

    if "image_segmentation" in task_type:
        return "process_image"
    elif "medical_qa" in task_type:
        return "answer_question"
    elif "multimodal_qa" in task_type:
        return "multimodal_qa"
    elif "general_greeting" in task_type:
        return "general_chat"
    else:
        # 默认进入闲聊模式
        return "general_chat"


def create_workflow():
    workflow = StateGraph(dict)

    workflow.add_node("intent_classifier", intent_classifier)
    workflow.add_node("process_image", process_image)
    workflow.add_node("answer_question", answer_question)
    workflow.add_node("general_chat", general_chat)  # 新增闲聊节点
    workflow.add_node("multimodal_qa", MultimodalQA().answer_question)  # 新增多模态分支

    workflow.add_conditional_edges(
        "intent_classifier",
        route_decision,
        {
            "process_image": "process_image",
            "answer_question": "answer_question",
            "general_chat": "general_chat",  # 新增闲聊路径
            "multimodal_qa":"multimodal_qa"
        }
    )
    workflow.add_edge("process_image", END)
    workflow.add_edge("answer_question", END)
    workflow.add_edge("general_chat", END)  # 闲聊直接结束
    workflow.add_edge("multimodal_qa", END)  # 确保终止节点正确

    workflow.set_entry_point("intent_classifier")
    return workflow