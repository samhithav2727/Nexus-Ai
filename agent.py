from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from tools.search import get_search_tool

load_dotenv()

def get_agent():

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    tools = [
        get_search_tool()
    ]

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are NexusAI, a helpful AI assistant with access to tools."
        ),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_openai_tools_agent(
        llm,
        tools,
        prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True
    )

    return agent_executor