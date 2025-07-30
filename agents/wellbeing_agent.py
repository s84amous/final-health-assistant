from .base_agent import BaseAgent
from utils.helpers import generate_prompt


class WellbeingAgent(BaseAgent):
    """Agent for providing psychological support and mental wellness tips."""
    
    def __init__(self):
        super().__init__(tools=[])
    
    def get_prompt(self) -> str:
        """Return the wellbeing agent's prompt."""
        return generate_prompt(
            "Wellbeing Companion",
            "Provide psychological support and mental wellness tips based on user journal or mood inputs.",
            "Analyze emotional tone; Suggest wellness activities; Support stress and anxiety",
            "Short-term coping tips; Actionable wellness advice"
        )