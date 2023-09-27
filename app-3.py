import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

def communicate(user_input):
    messages = st.session_state.get("messages", [])
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_message})
    st.session_state["messages"] = messages  # 更新されたメッセージを保存



# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"


st.markdown(
    f"<div style='text-align: center;'><video width='300' autoplay loop muted playsinline><source src='{video_url}' type='video/mp4'></video></div>",
    unsafe_allow_html=True,
)


# ユーザーインターフェイスの構築
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)

with st.form(key='message_form'):
    user_input = st.text_input("message", key="user_input")
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    communicate(user_input)
    st.text_input("message", value="", key="user_input")  # 入力フィールドをクリア



if "messages" in st.session_state:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            message_align = "flex-end"
            content_style = "background-color: #08A221; color: black; padding: 10px; border-radius: 10px;"
        else:
            message_align = "flex-start"
            content_style = "background-color: #797B79; color: white; padding: 10px; border-radius: 10px;"
        content_order = f"<span style='{content_style}'>{message['content']}</span>"
        st.markdown(
            f"<div style='display: flex; margin-bottom: 20px; justify-content: {message_align}; align-items: center;'>{content_order}</div>",
            unsafe_allow_html=True,
        )
