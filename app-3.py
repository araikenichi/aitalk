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




# StreamlitのMarkdownでCSSを適用
st.markdown(
    f"""
    <style>
        .message-box {{
            position: relative;
            background-color: #797B79;  # グレー
            padding: 10px;
            border-radius: 10px;
        }}
        .message-box.green {{
            background-color: #08A221;  # 緑
        }}
        .message-box::after {{
            content: "";
            position: absolute;
            width: 0;
            height: 0;
            border-style: solid;
        }}
        .message-box.green::after {{
            border-color: #08A221 transparent transparent transparent;
            border-width: 10px 10px 0 0;
            top: 100%;
            left: 50%;
        }}
        .message-box::after {{
            border-color: #797B79 transparent transparent transparent;
            border-width: 10px 10px 0 0;
            top: 100%;
            left: 20%;
        }}
    </style>
    <div class="message-box">
        グレーのメッセージ
    </div>
    <div class="message-box green">
        緑のメッセージ
    </div>
    """,
    unsafe_allow_html=True,
)
