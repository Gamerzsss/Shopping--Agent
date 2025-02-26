# agents.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import BaseTool
from tavily import TavilyClient
from config import get_gemini_api_key, get_tavily_api_key

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=get_gemini_api_key())
tavily_client = TavilyClient(api_key=get_tavily_api_key())

class TavilySearchTool(BaseTool):
    name: str = "Tavily Search"
    description: str = "Useful for searching the internet for information."

    def _run(self, query: str) -> str:
        """Use the Tavily API to search for the query."""
        try:
            results = tavily_client.search(query)
            return str(results)
        except Exception as e:
            return f"Error during Tavily search: {e}"

    async def _arun(self, query: str) -> str:
        """Use the Tavily API to search for the query asynchronously."""
        try:
            results = tavily_client.search(query)
            return str(results)
        except Exception as e:
            return f"Error during Tavily search: {e}"

tools = [TavilySearchTool()]

product_researcher = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

price_comparator = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

shopping_list_manager = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

order_placement_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

user_interface_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

quality_inspection_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

shipping_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)

after_sales_agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, handle_parsing_errors=True
)