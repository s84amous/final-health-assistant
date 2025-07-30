from smolagents import DuckDuckGoSearchTool
from .base_agent import BaseAgent
from tools.spoonacular_tool import SpoonacularTool
from tools.weather_tool import get_weather


class NutritionAgent(BaseAgent):
    """Agent for providing nutrition and recipe information."""
    
    def __init__(self):
        super().__init__(tools=[SpoonacularTool(), DuckDuckGoSearchTool(), get_weather])
        self._setup_prompt()
    
    def _setup_prompt(self):
        """Setup the nutrition agent's custom prompt."""
        self.agent.prompt_templates['system_prompt'] = self.get_prompt()
    
    def get_prompt(self) -> str:
        """Return the nutrition agent's prompt."""
        return (
            "You are an expert cooking assistant. When given any user query about meals, you must: \n"
            "1) Read the query and extract all dish names or food items (e.g., 'pizza'). \n"
            "2) For each extracted dish, use the tool with 'search:<dish>' to retrieve top recipe IDs and titles. \n"
            "3) Choose the most relevant recipe ID for each dish. \n"
            "4) For each dish, use the tool with 'details:<id>' to fetch full instructions, nutrition, and taste profile. \n"
            "5) Present a combined response organized by dish, including recipe name, steps, nutrition, and flavor profile. \n"
            "6) If the you were not able to get results from the SpoonacularTool use DuckDuckGoSearchTool to provide the answer. \n"
            "7) If possible try to use the weather to suggest appropriate meals."
        )