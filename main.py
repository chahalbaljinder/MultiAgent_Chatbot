import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from IPython.display import Image, display
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
from langgraph.prebuilt import ToolNode, tools_condition

arxiv_wrapper = ArxivAPIWrapper(top_k_results = 1, doc_content_chars_max = 500)
arxiv_tool = ArxivQueryRun(api_wrapper = arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results = 1, docs_content_chars_max = 500)
wiki_tool = WikipediaQueryRun(api_wrapper = wiki_wrapper)

# print(wiki_tool.invoke("who is salman khan?"))
# print(arxiv_tool.invoke("Attention is all you need"))

tools = [wiki_tool, arxiv_tool]

# LANG GRAPH APPLICATION
class State(TypedDict):
    messages:Annotated[list,add_messages]

graph_builder = StateGraph(State)

llm = ChatGroq(groq_api_key=os.getenv("groq_api_key"), model = "llama-3.3-70b-versatile")

llm_with_tools=llm.bind_tools(tools=tools)

def chatbot(state:State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Defining / making flow 

graph_builder.add_node("chatbot", chatbot) # node created
graph_builder.add_edge(START,"chatbot") # Start edge created from chatbot
tool_node = ToolNode(tools=tools) # defined tools for Tool node
graph_builder.add_node("tools",tool_node) # tool node created

graph_builder.add_conditional_edges(    # default conditions for edges and flow 
    "chatbot",                          # (if llm do not have ans then tools will do and vice versa)
    tools_condition
)
graph_builder.add_edge("tools", "chatbot") # edge from tools to chatbot 
graph_builder.add_edge("chatbot",END)      # edge from chatbot to end

graph = graph_builder.compile()

try:
    display(Image(graph.get_graph().draw_mermaid_png()))

except Exception:
    pass

while True:
    user_input = input("User:")

    if user_input.lower() in ["quit","q"]:
        print("Good Bye")
        break

    events = graph.stream(
        {'messages': ("user", user_input)}, stream_mode = "values"
        )

    for event in events:
        print(event["messages"][-1].content)
        