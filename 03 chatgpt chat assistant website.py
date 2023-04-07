import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a chiropractor that specializes in expplaining complex concepts to people like they're five"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "YOTO Chiro")

demo.launch(share=True)