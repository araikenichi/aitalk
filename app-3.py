import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key







# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を削除


# ユーザーインターフェイスの構築
st.write()
# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)





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







# ユーザー入力
user_input = st.text_input("message", key="user_input", on_change=communicate)
# ...

# チャットボットとのコミュニケーション
def communicate(new_input):
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": new_input}
    messages.append(user_message)
    
    # OpenAI APIを使用した応答生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_message})


# ユーザーが新しいメッセージを入力した場合にcommunicate関数を呼び出す
if user_input:
    communicate(user_input)
    st.session_state["user_input"] = None  # 入力欄を消去




# 初期化部分
if "messages" not in st.session_state:
    st.session_state["messages"] = []



if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            message_align = "flex-end"
            content_style = "background-color: #0DAB26; color: white; padding: 10px; border-radius: 10px;"
            tail_svg = """<svg height='20' width='50' style='position: absolute; right: 40; bottom: 0;'><polygon points='0,0 20, 20,0' style='fill:#0DAB26;'></polygon></svg>"""
        else:
            message_align = "flex-start"
            content_style = "background-color: #ACAFAC; color: white; padding: 10px; border-radius: 10px;"
            tail_svg = """<svg height='70' width='40' style='position: absolute; left: 40; bottom: 0;'><polygon points='0,0 20,0 0,20' style='fill:#ACAFAC;'></polygon></svg>"""

        content_order = f"<span style='position: relative; {content_style}'>{message['content']}{tail_svg}</span>"

        st.markdown("""
<style>
    .chat-bubble {
        position: relative;
        background-color: #ACAFAC;  /* Gray background for assistant */
        border-radius: 10px;
        padding: 10px;
        width: fit-content;
        margin-bottom: 10px;
    }
    .chat-bubble-user {
        background-color: #0DAB26;  /* Green background for user */
        color: white;
    }
    .chat-bubble::before {
        content: "";
        position: absolute;
        width: 0;
        height: 0;
        left: -10px;
        bottom: 0;
        border: 5px solid transparent;
        border-right-color: #ACAFAC;  /* Gray background for assistant */
    }
    .chat-bubble-user::before {
        left: auto;
        right: -10px;
        border-left-color: #0DAB26;  /* Green background for user */
        border-right-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-bubble">你好，有什么可以帮助您的？</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-bubble chat-bubble-user">你好，我有个问题。</div>', unsafe_allow_html=True)
