from .base_agent import BaseAgent
from tools.weather_tool import get_weather
from utils.helpers import generate_prompt


class FitnessAgent(BaseAgent):
    """Agent for providing fitness and workout recommendations."""
    
    def __init__(self):
        super().__init__(tools=[get_weather])
    
    def get_prompt(self) -> str:
        """Return the fitness agent's prompt."""
        return generate_prompt(
            "Fitness Coach",
            "Provides tailored workout recommendations based on user requests and environmental factors to have a complete workout or help the user with his fitness requests.",
            "Use weather and activity history; Recommend suitable fitness activities and help the user with his requests",
            "A personalized activity suggestion"
        )