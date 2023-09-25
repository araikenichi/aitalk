import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    system_prompt = """
    あなたは僕の彼女とします、僕を恋人として接してください、...
    """
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
    ]

# チャットボットとやりとりする関数
def communicate(new_input=None):
    messages = st.session_state["messages"]
    if new_input:
        user_message = {"role": "user", "content": new_input}
        messages.append(user_message)
    
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_message = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": bot_message})

# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)

# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"


# ユーザー入力
user_input = st.text_input("message", key="user_input")

# ユーザーが新しいメッセージを入力した場合にcommunicate関数を呼び出す
if user_input:
    communicate(user_input)
    st.session_state["user_input"] = ""  # 入力欄を消去






# メッセージ表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):






if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            message_align = "flex-end"
            content_style = "background-color: #08A221; color: black; padding: 10px; border-radius: 10px;"
            content_order = f"<span style='{content_style}'>{message['content']}</span>"
        else:
            message_align = "flex-start"
            content_style = "background-color: #797B79; color: white; padding: 10px; border-radius: 10px;"
            content_order = f"<span style='{content_style}'>{message['content']}</span>"

        st.markdown(
            f"<div style='display: flex; margin-bottom: 20px; justify-content: {message_align}; align-items: center;'>{content_order}</div>",
            unsafe_allow_html=True,
        )

