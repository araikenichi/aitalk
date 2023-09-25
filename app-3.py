import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# Session state初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": ""}]

# コミュニケーション関数
def communicate(new_input, language="English"):
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": new_input}
    messages.append(user_message)

    # OpenAI APIを使用して応答生成
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    bot_content = response['choices'][0]['message']['content']
    bot_message = {"role": "assistant", "content": f"{bot_content}"}
    messages.append(bot_message)
    st.session_state["messages"] = messages

# UI部分
st.markdown("<h1 style='text-align: center;'>LISA</h1>", unsafe_allow_html=True)

# ユーザー入力
user_input = st.text_input("message", key="unique_user_input", on_change=communicate)

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
