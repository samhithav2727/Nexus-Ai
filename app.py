import streamlit as st
from agent import get_agent

st.set_page_config(page_title="NexusAI", page_icon="🧠")
st.title("🧠 NexusAI Agent")
st.caption("Powered by LangChain + OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    st.chat_message(role).write(msg)

user_input = st.chat_input("Ask NexusAI anything...")

if user_input:
    st.chat_message("user").write(user_input)
    with st.spinner("NexusAI is thinking..."):
        agent = get_agent()
        response = agent.invoke({"input": user_input})
        answer = response["output"]
    st.chat_message("assistant").write(answer)
    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("assistant", answer))
