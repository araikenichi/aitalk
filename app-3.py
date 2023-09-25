import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key


# プレースホルダーの作成
input_placeholder = st.empty()





# チャットボットとのコミュニケーション
def communicate(new_input):
    messages = st.session_state.get("messages", [])
    user_message = {"role": "user", "content": new_input}
    messages.append(user_message)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_message})
    st.session_state["messages"] = messages

# メッセージの表示
if st.session_state.get("messages"):
    messages = st.session_state.get("messages")
    for message in messages:
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



# ユーザーインターフェイスの構築
st.write()
# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)


# ユーザー入力
user_input = input_placeholder.text_input("Message", key="user_input")
if user_input:
    communicate(user_input)
  if user_input:
    communicate(user_input)
    st.session_state["user_input"] = ""  # エラーを避けるための修正点




# カスタムCSS
st.markdown("""
    <style>
        .stTextInput input {
            box-shadow: 0px 0px 5px grey;
        }
    </style>
    """, unsafe_allow_html=True)



# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = []


from PIL import Image  # PILライブラリからImageクラスをインポート
import requests
from io import BytesIO
import streamlit as st


# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"

st.markdown(
    f"<div style='text-align: center;'><video width='300' autoplay loop muted playsinline><source src='{video_url}' type='video/mp4'></video></div>",
    unsafe_allow_html=True,
)









# 初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = []





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
