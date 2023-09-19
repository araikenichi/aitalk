
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "AI Talk"}
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

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.write("")
# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>Chat Talk</h1>", unsafe_allow_html=True)


from PIL import Image
import streamlit as st

# ユーザーインターフェイスの構築
st.markdown("<h1 style='text-align: center;'>Chat Talk</h1>", unsafe_allow_html=True)

# 画像の読み込み
try:
    image_path = "/Users/araikenichi/Downloads/girlcute.png"  # 画像ファイルのフルパスを指定
    image = Image.open(image_path)
    # 画像を中央に表示
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image, caption='', use_column_width=True)
    st.write("</div>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Image file not found.")



user_input = st.text_input("message", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
