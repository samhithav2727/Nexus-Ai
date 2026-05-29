from langchain.tools import Tool
from duckduckgo_search import DDGS

def search_web(query):

    results = DDGS().text(query, max_results=3)

    output = ""

    for result in results:
        output += result["title"] + "\n"
        output += result["body"] + "\n\n"

    return output

def get_search_tool():

    return Tool(
        name="Web Search",
        func=search_web,
        description="Search the web for current information"
    )