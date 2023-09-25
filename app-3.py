import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# UI部分
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)

# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"
st.markdown(
    f"<div style='text-align: center;'><video width='300' autoplay loop muted><source src='{video_url}' type='video/mp4'></video></div>",
    unsafe_allow_html=True,
)

# Session state初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = []



    system_prompt = """
この""内のがあなたの設定です"年齢は20歳、身長168cm、体重50kg、中国出身、中国上海人、性格明るい、かわいい系、学校の先生、中国語、英語、日本語がネイティブ、これらを教えている。


* 政治
* 敏感な歴史
* 犯罪　
これらの話題は禁止します、聞かれてもことえないでください

"""
# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
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




# ユーザー入力
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

user_input = st.text_input("message", value=st.session_state["user_input"], key="unique_user_input")

if user_input:
    st.session_state["user_input"] = user_input
    communicate()
    st.session_state["user_input"] = ""

# メッセージ表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            content_style = "background-color: #0DAB26; color: black; padding: 10px; border-radius: 10px; position: relative;"
            align_style = "flex-end"
        else:
            content_style = "background-color: #ACAFAC; color: white; padding: 10px; border-radius: 10px; position: relative;"
            align_style = "flex-start"

        content = message['content']
        st.markdown(
            f"""
            <div style='display: flex; justify-content: {align_style}; align-items: center;'>
                <div style='{content_style}'>
                    {content}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
