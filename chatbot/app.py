import gradio as gr
import config
from transformers import pipeline


emo_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)


def chatbot(user_input, history=[]):
    history = history or []
    messages = [{"role": "system", "content": "You"}]
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})
    
    messages.append({"role": "user", "content": user_input})
    bot_response = config.chat(messages)

    history.append((user_input, bot_response))
    return history, history


def emotion_chatbot(user_input, history=[]):
    output = emo_classifier(user_input)[0]

    print(output)

    sorted_output = sorted(output, key=lambda x: x['score'], reverse=True)
    max_emotion = sorted_output[0]['label']

    history.append((user_input, f"Your emotion is {max_emotion}."))
    return history, history

with gr.Blocks() as app:
    mode = gr.State("chat")
    def switch_mode():
        mode.value = "emotion" if mode.value == "chat" else "chat"
        text = "Now is chat mode, click to convert to emotion mode" if mode.value == "chat" else "Now is emotion mode, click to convert to chat mode"
        return (mode, text)

    gr.Markdown("## multi-function chatbot")
    chat_box = gr.Chatbot()
    user_input = gr.Textbox(placeholder="input your question...")
    switch_btn = gr.Button("Now is chat mode, click to convert to emotion mode")

    def handle_input(user_input, history):
        if mode.value == "emotion":
            print("emotion")
            return emotion_chatbot(user_input, history) + ("",)
        print("chat")
        return chatbot(user_input, history) + ("",)

    user_input.submit(handle_input, [user_input, chat_box], [chat_box, chat_box, user_input])
    switch_btn.click(switch_mode, None, [mode, switch_btn])

if __name__ == "__main__":
    app.launch()
