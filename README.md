🤖 NexusAI Assistant
A conversational AI assistant built for humans — not just developers.
Ask it anything. It streams back answers in real time, remembers your conversation, and doesn't make you read a manual first.

What is NexusAI?
NexusAI is a clean, no-frills AI chat interface powered by OpenAI's language models and built with Streamlit + LangChain. It came out of a simple frustration: most AI wrappers are either too bare-bones or bloated with features no one asked for.

This one hits the middle — fast to set up, nice to use, and easy to extend. Whether you're prototyping ideas, learning about LLMs, or just want a local GPT-powered assistant, NexusAI gets out of the way and lets you focus on the conversation.

Features
Chat interface
Clean, minimal UI that just works out of the box
Streaming responses
Answers appear as they're generated — no waiting
Model selector
Switch between GPT models without touching the code
Temperature control
Dial creativity up or down to fit your use case
Session memory
Keeps the full conversation in context during a session
Secure API keys
Loaded from .env — never hardcoded, never committed
Tech stack
Streamlit
LangChain
OpenAI API
Python 3.9+
python-dotenv
Getting started
Clone the repo, add your API key, and you're talking to GPT in under two minutes.

git clone https://github.com/your-username/NexusAI.git
cd NexusAI
pip install -r requirements.txt
Create a .env file in the root directory:

OPENAI_API_KEY=your-api-key-here
Then run:

streamlit run app.py
How it works
1
You type a message in the chat window
2
NexusAI forwards your query — along with the full conversation history — to the selected OpenAI model via LangChain
3
The model generates a response, and you see it streamed back word by word — no loading spinner, no delay
4
The conversation stays in memory for the session, so follow-up questions actually make sense
Use cases
NexusAI is general-purpose on purpose. Here's what people typically use it for, though it won't stop you from finding your own:

coding help
research & learning
content drafting
brainstorming
day-to-day productivity
