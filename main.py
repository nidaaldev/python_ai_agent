import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", api_key=api_key)
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
        ("placeholder", "{chat_history}"),
        ("human", "{query} {name}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools = []
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"query": "What is the capital of France", "name": "Alice"})


try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response.summary)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)
