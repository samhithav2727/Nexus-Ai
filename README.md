🤖 NexusAI Assistant

An AI-powered conversational assistant built using Streamlit, LangChain, and OpenAI. NexusAI provides a seamless chat experience with real-time AI responses, customizable model settings, and an intuitive interface for asking questions, generating content, solving problems, and exploring ideas.

🌐 Live Demo

👉 https://nexus-ai-agent.streamlit.app

✨ Features

📌 Clean and interactive chat interface

💬 Ask questions in natural language

🤖 Powered by OpenAI GPT models

⚙️ Choose between different AI models

🎛️ Adjust response creativity with temperature controls

⚡ Real-time streaming responses

📝 Session-based conversation history

🗑️ One-click chat reset functionality

🛠️ Tech Stack
Tool	Purpose
Streamlit	Web UI
LangChain	LLM Integration
OpenAI GPT	Language Model
Python	Backend Development
python-dotenv	Environment Management
📁 Project Structure
NexusAI/
├── app.py              ← Main Streamlit application
├── agent.py            ← AI agent logic
├── requirements.txt    ← Dependencies
├── README.md           ← Documentation
├── .gitignore
└── tools/              ← Utility modules
⚙️ Run Locally
1. Clone the repository
git clone https://github.com/samhithav2727/Nexus-Ai.git
cd Nexus-Ai
2. Install dependencies
pip install -r requirements.txt
3. Add your API key

Create a .env file:

OPENAI_API_KEY=your-api-key-here
4. Run the application
streamlit run app.py
🔑 Environment Variables
Variable	Description
OPENAI_API_KEY	Your OpenAI API Key
💡 How It Works
User enters a prompt through the chat interface.
NexusAI sends the request to the selected OpenAI model using LangChain.
The language model generates a response.
Responses are streamed in real time to improve user experience.
Chat history is maintained throughout the session.
🚀 Future Enhancements
RAG-based document question answering
PDF upload and analysis
Web search integration
Memory-enabled conversations
Multi-agent workflows
Voice interaction support
👨‍💻 Author

samhithav2727 — GitHub
