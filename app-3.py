import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key



# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": ""}
        ]



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
st.write("")
# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)








from PIL import Image  # PILライブラリからImageクラスをインポート
import requests
from io import BytesIO
import streamlit as st


# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"

st.markdown(
    f"<div style='text-align: center;'><video width='300' autoplay loop muted><source src='{video_url}' type='video/mp4'></video></div>",
    unsafe_allow_html=True,
)





# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = []

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








# 既存のStreamlitアプリのコード
# ...

# カスタムCSSを適用
st.markdown("""
<style>
    /* AIbot側のメッセージスタイル */
    .bot-message {
        background-color: #2c2c2c;  /* 背景色 */
        color: white;  /* 文字色 */
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
    /* ユーザ側のメッセージスタイル */
    .user-message {
        background-color: green;  /* 背景色 */
        color: black;  /* 文字色 */
        padding: 10px;
        border-radius: 10px;
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 既存のメッセージ表示ロジック
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            # ユーザのメッセージ
            st.markdown(f"<div class='user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            # AIbotのメッセージ
            st.markdown(f"<div class='bot-message'>{message['content']}</div>", unsafe_allow_html=True)
