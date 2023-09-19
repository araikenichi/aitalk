
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



from PIL import Image  # PILライブラリからImageクラスをインポート
import requests
from io import BytesIO
import streamlit as st


# 画像のURL
image_url = "https://user-images.githubusercontent.com/37874452/268891476-c11a2c43-8409-4b14-b770-6e6ba7360ab2.png"

# 画像をダウンロード
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))


# 画像を中央に表示するためのCSSを適用
st.markdown(
    f"<div style='text-align: center;'><img src='https://user-images.githubusercontent.com/37874452/268891476-c11a2c43-8409-4b14-b770-6e6ba7360ab2.png' width='300'></div>",
    unsafe_allow_html=True,
)





# ユーザー入力
user_input = st.text_input("message", key="user_input")

# チャットボットとのコミュニケーション
def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)
    # OpenAI APIを使用した応答生成（ここは適宜調整）
    # 省略

# ユーザーが新しいメッセージを入力した場合にcommunicate関数を呼び出す
if user_input:
    communicate()

# メッセージの表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            speaker = "🙂"
        else:
            speaker = f"<img src='https://user-images.githubusercontent.com/37874452/268891476-c11a2







        st.write(speaker + ": " + message["content"])
