

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



# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270180987-85b8c0b5-5ba2-4862-b5cb-2e746eb771ec.mp4"

# HTMLとJavaScriptを使用して動画を自動再生・ループ再生
video_html = f'''
<video width="320" height="240" controls autoplay loop>
    <source src="{video_url}" type="video/mp4">
</video>
'''

# StreamlitにHTMLを埋め込む
st.markdown(video_html, unsafe_allow_html=True)

# ... 以降はそのまま




if st.session_state["messages"]:
    messages = st.session_state["messages"]
    # メッセージ表示のコード

    # ユーザーまたはチャットボットの最新のメッセージに基づいて画像を選択
    last_message = messages[-1]['content'].lower()  # 最新のメッセージを取得
    if "happy" in last_message:
        current_image_url = happy_image_url
    elif "sad" in last_message:
        current_image_url = sad_image_url
    else:
        current_image_url = neutral_image_url

    # 画像をダウンロード
    response = requests.get(current_image_url)
    image = Image.open(BytesIO(response.content))

    # 画像を表示
    st.image(image)

    # ...（以降のメッセージ表示コード）
