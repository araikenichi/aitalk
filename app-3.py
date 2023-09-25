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
あなたは僕の彼女とします、僕を恋人として接してください、あなたの年齢は20歳、身長168cm、体重50kg、中国出身、中国上海人、性格明るい、かわいい系、学校の先生、中国語、英語、日本語がネイティブ、これらを教えている。


* 政治
* 敏感な歴史
* 犯罪　
これらの話題は禁止します、聞かれてもことえないでください

"""

# st.session_stateを使いメッセージのやりとりを保存
def communicate(user_input):
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": user_input}
    messages.append(user_message)
    
    # OpenAI APIを使用した応答生成（適宜調整してください）
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_message})



# ユーザー入力
if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

user_input = st.text_input("Message", value=st.session_state["user_input"])


if user_input:
    communicate(user_input)
    st.session_state["user_input"] = ""




# メッセージ表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]
    for message in reversed(messages):
        if message["role"] == "user":
            align_style = "flex-end"
            content_style = "background-color: #0DAB26; color: black; padding: 10px; border-radius: 10px; position: relative;"
        else:
            align_style = "flex-start"
            content_style = "background-color: #ACAFAC; color: white; padding: 10px; border-radius: 10px; position: relative;"
        
        content = message['content']
        st.markdown(
            f"<div style='display: flex; justify-content: {align_style}; align-items: center;'>\
                <div style='{content_style}'>{content}</div>\
            </div>",
            unsafe_allow_html=True,
        )
        
