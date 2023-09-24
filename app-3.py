

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





# ...（先頭のコードはそのまま）

# 画像のURLを変数に格納（実際のURLに書き換えてください）
happy_image_url = "https://example.com/happy.png"
sad_image_url = "https://example.com/sad.png"
neutral_image_url = "https://example.com/neutral.png"

if st.session_state["messages"]:
    messages = st.session_state["messages"]
    
    # ユーザーまたはチャットボットの最新のメッセージに基づいて画像を選択
    last_message = messages[-1]['content'].lower()  # 最新のメッセージを取得
    if "happy" in last_message:
        current_image_url = happy_image_url
    elif "sad" in last_message:
        current_image_url = sad_image_url
    else:
        current_image_url = neutral_image_url

    # 画像を表示
    st.image(current_image_url)

    # メッセージの表示
    for message in reversed(messages):
        if message["role"] == "user":
            message_style = "background-color: #DCF8C6; border-radius: 12px; padding: 10px; display: inline-block; color: black;"
            message_align = "flex-end"
        else:
            message_style = "background-color: #333333; border-radius: 12px; padding: 10px; display: inline-block; color: white;"
            message_align = "flex-start"

        st.markdown(
            f"<div style='display: flex; justify-content: {message_align}; margin-bottom: 12px;'><div style='{message_style}'>{message['content']}</div></div>",
            unsafe_allow_html=True,
        )
