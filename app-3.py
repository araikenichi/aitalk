import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key







def communicate(new_input):
    messages = st.session_state.get("messages", [])
    user_message = {"role": "user", "content": new_input}
    messages.append(user_message)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": bot_message})
    st.session_state.messages = messages
    st.session_state["user_input"] = ""



# タイトルを中央に表示
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)



# スペーサーでメッセージを下に押し出す
for _ in range(20):
    st.empty()



# 動画のURL
video_url = "https://user-images.githubusercontent.com/37874452/270353369-38139a9d-2428-454e-956a-23d860d5a6fc.mp4"

st.markdown(
    f"<div style='text-align: center;'><video width='300' autoplay loop muted playsinline><source src='{video_url}' type='video/mp4'></video></div>",
    unsafe_allow_html=True,
)





# ユーザー入力（メッセージバーに影をつけるCSSを適用）
user_input = st.text_input(
    "Message", 
    key="user_input", 
    value=st.session_state.get("user_input", ""),
    help="Type your message here"
)
st.markdown(
    "<style>div[data-baseweb='input'] { box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.2); }</style>",
    unsafe_allow_html=True,
)

if user_input:
    communicate(user_input)




if st.session_state.get("messages"):
    messages = st.session_state.messages
    for message in messages:
        if message["role"] == "user":
            message_align = "flex-end"
            content_style = "background-color: #0DAB26; color: white; padding: 10px; border-radius: 10px; position: relative;"
        else:
            message_align = "flex-start"
            content_style = "background-color: #ACAFAC; color: white; padding: 10px; border-radius: 10px; position: relative;"

        content_order = f"<div style='{content_style}'>{message['content']}</div>"

        st.markdown(
            f"<div style='display: flex; margin-bottom: 20px; justify-content: {message_align}; align-items: center;'>{content_order}</div>",
            unsafe_allow_html=True,
        )
