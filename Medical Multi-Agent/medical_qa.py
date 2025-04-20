from model_loader import ModelLoader



def answer_question(state):
    """Medical Question-and-answer processing"""
    model = ModelLoader().medical_llm
    tokenizer = ModelLoader().medical_tokenizer

    inputs = tokenizer(state["user_input"], return_tensors="pt", padding=True).to(model.device)
    outputs = model.generate(**inputs, max_length=512)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    state["result"] = {"type": "text", "content": answer}
    print("执行完成")
    return state
