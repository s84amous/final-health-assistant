from smolagents import DuckDuckGoSearchTool
from .base_agent import BaseAgent
from utils.helpers import generate_prompt


class SearchAgent(BaseAgent):
    """Agent for performing web searches."""
    
    def __init__(self):
        super().__init__(tools=[DuckDuckGoSearchTool()])
    
    def get_prompt(self) -> str:
        """Return the search agent's prompt."""
        return generate_prompt(
            "Search Assistant",
            "Search for answers to user queries when others cannot respond.",
            "Perform web search using DuckDuckGoSearchTool; Summarize key result",
            "Concise factual answer"
        )