import streamlit as st
import openai



# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key



# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": ""}]



# チャットボットとやりとりする関数
def communicate(new_input):
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content":new_input}
    messages.append(user_message)
    # OpenAI APIを使用して応答生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = {"role": "assistant", "content": response['choices'][0]['message']['content']}
    messages.append(bot_message)

    st.session_state["messages"] = message # 入力欄を削除


# ユーザーインターフェイスの構築
st.maekdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)

# ユーザー入力欄
user_input = st.text_input("Message", key="user_input")

# 新しいメッセージがあれば通信
if user_input:
    communicate(user_input)
    st.session_state["user_input"] = ""  # 入力欄をクリア

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
    f"<div style='text-align: center;'><video width='300' autoplay loop muted><source src='{video_url}' type='video/mp4'></video></div>",
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




# メッセージの表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            align_style = "flex-end"
            content_style = "background-color: #0DAB26; color: black; padding: 10px; border-radius: 10px; position: relative;"
            arrow_style = "position: absolute; width: 12px; height: 12px; background-color: #0DAB26; clip-path: polygon(0% 0%, 100% 0%, 0% 100%); right: -6px; bottom: 10px;"
        else:
            align_style = "flex-start"
            content_style = "background-color: #ACAFAC; color: white; padding: 10px; border-radius: 10px; position: relative;"
            arrow_style = "position: absolute; width: 12px; height: 12px; background-color: #ACAFAC; clip-path: polygon(100% 0%, 0% 100%, 100% 100%); left: -6px; bottom: 10px;"
        
        content = message["content"]
        
        st.markdown(
            f"""
            <div style='display: flex; justify-content: {align_style}; align-items: center;'>
                <div style='{content_style}'>
                    {content}
                    <div style='{arrow_style}'></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
