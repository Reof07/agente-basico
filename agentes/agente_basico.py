
from langgraph.prebuilt import create_react_agent

from agentes.tools import tavily_search_tool
from core.config import model

#tools
tools = [tavily_search_tool]


graph = create_react_agent(model, tools=tools)
