import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="NexusAI",
    page_icon="🤖",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .stChatMessage {
        border-radius: 12px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 NexusAI Assistant")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    model = st.selectbox(
        "Choose Model",
        ["gpt-3.5-turbo", "gpt-4"]
    )

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

# Chat input
user_input = st.chat_input("Ask NexusAI anything...")

# Handle user input
if user_input:

    # Save user message
    st.session_state.messages.append(("user", user_input))

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Initialize LLM
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
        streaming=True
    )

    # Display assistant response
    with st.chat_message("assistant"):

        response_placeholder = st.empty()
        full_response = ""

        try:
            for chunk in llm.stream([
                HumanMessage(content=user_input)
            ]):

                if chunk.content:
                    full_response += chunk.content
                    response_placeholder.write(full_response)

        except Exception as e:
            full_response = f"Error: {str(e)}"
            response_placeholder.error(full_response)

    # Save assistant response
    st.session_state.messages.append(
        ("assistant", full_response)
    )