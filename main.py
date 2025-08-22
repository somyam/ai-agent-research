from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from tools import *
load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

class ResearchChain:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"), #autofilled by agent executor
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"), #autofilled by agent executor
    ]
).partial(format_instructions=parser.get_format_instructions())

tools=[search_tool, wikipedia_tool, save_tool]
agent=create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor=AgentExecutor(agent=agent, tools=tools, verbose=True)
query=input("What can I help you research?")
raw_response=agent_executor.invoke({"query": query})

# Parse the response to get the ResearchResponse object
try:
    structured_response = parser.parse(raw_response.get("output"))
    print("\n=== Research Response ===")
    print(f"Topic: {structured_response.topic}")
    print(f"Summary: {structured_response.summary}")
    print(f"Sources: {structured_response.sources}")
    print(f"Tools Used: {structured_response.tools_used}")
except Exception as e:
    print(f"Failed to parse response: {e}")
    print("Raw output:", raw_response.get("output"))