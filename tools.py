from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from datetime import datetime

#use this file to add API -> wrap them in tool annotation and use them with llm

search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """Search the web for the latest information on a given topic"""
    return search.run(query)

wikipedia_api=WikipediaAPIWrapper(top_k_results=3)

@tool
def wikipedia_tool(query: str) -> str:
    """Search the wikipedia for the latest information on a given topic"""
    return wikipedia_api.run(query)

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

@tool
def save_tool(query: str) -> str:
    """Save the information to a file"""
    return save_to_txt.run(query)
