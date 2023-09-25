import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key



# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": ""}
        ]



def communicate(new_input, language):
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": new_input}
    messages.append(user_message)

    # OpenAI APIを使用して応答生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_content = response['choices'][0]['message']['content']

    # 言語ごとに異なる「お姉さん風」の応答
    if language == "English":
        bot_message = {
            "role": "assistant",
            "content": f"Sure, darling! 💕 {bot_content} How does that sound? ✨"
        }
    elif language == "日本語":
        bot_message = {
            "role": "assistant",
            "content": f"わかったわ、ちゃんと聞いてるからね！💕 {bot_content} どうかしら、大丈夫？✨"
        }
    elif language == "中文":
        bot_message = {
            "role": "assistant",
            "content": f"明白了，亲爱的！💕 {bot_content} 怎么样，满意吗？✨"
        }

    messages.append(bot_message)
    st.session_state["messages"] = messages

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




if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            message_align = "flex-end"
            content_style = "background-color: #0DAB26; color: black; padding: 10px; border-radius: 10px;"
            content_order = f"<span style='{content_style}'>{message['content']}</span>"
        else:
            message_align = "flex-start"
            content_style = "background-color:#ACAFAC; color: white; padding: 10px; border-radius: 10px;"
            content_order = f"<span style='{content_style}'>{message['content']}</span>"

        st.markdown(
            f"<div style='display: flex; margin-bottom: 20px; justify-content: {message_align}; align-items: center;'>{content_order}</div>",
            unsafe_allow_html=True,
        )
