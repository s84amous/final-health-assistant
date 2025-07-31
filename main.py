import warnings
import os
import sys
import logging
from typing import Dict, List
from agents import (
    WellbeingAgent, FitnessAgent, NutritionAgent, 
    ReminderAgent, SearchAgent, RouterAgent
)
from tools.weather_tool import get_weather
from utils.helpers import parse_router_output, invoke_agent # pyright: ignore[reportAssignmentType]

# suppress all warnings at all levels
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")
os.environ['PYTHONWARNINGS'] = 'ignore'
os.environ['PYTHONHASHSEED'] = '0'

class SuppressStderr:
    def __enter__(self):
        self.original_stderr = sys.stderr
        sys.stderr = open(os.devnull, 'w')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self.original_stderr

# aggressive logging suppression
logging.getLogger().setLevel(logging.CRITICAL)
for logger_name in ['pydantic', 'httpx', 'litellm', 'urllib3', 'smolagents', 'asyncio']:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.CRITICAL)
    logger.disabled = True
    logger.propagate = False


class AgentOrchestrator:
    """Orchestrates the routing and execution of specialized agents."""
    
    def __init__(self):
        self.router_agent = RouterAgent()
        self.agents = {
            "Wellbeing": WellbeingAgent(),
            "Fitness": FitnessAgent(),
            "Nutrition": NutritionAgent(),
            "Reminder": ReminderAgent(),
            "Search": SearchAgent()
        }
    
    def process_request(self, user_input: str, location: Dict[str, float]) -> List[str]:
        """Process user request and return responses from appropriate agents."""
        print("\n--- ROUTER INPUT ---")
        print(f"Input: {user_input}")
        
        # weather context
        ctx = {}
        weather_info = get_weather({"location": location}, ctx)
        
        if "error" not in weather_info: # pyright: ignore[reportOperatorIssue]
            weather_text = (
                f"Current weather in {weather_info['city']}: {weather_info['temp']}°C, " # pyright: ignore[reportIndexIssue]
                f"{weather_info['condition']}" # pyright: ignore[reportIndexIssue]
            )
        else:
            weather_text = "Weather info unavailable"
        
        print("\n[Weather Context]", weather_text)
        
        # route the request - suppress stderr during execution
        full_prompt = self.router_agent.get_prompt() + f"\nUser Input: {user_input}"
        with SuppressStderr():
            router_output = self.router_agent.run(full_prompt)
        
        # parse router output
        categorized_inputs = parse_router_output(router_output)
        print("Categorized inputs:", categorized_inputs)
        
        # process each category
        responses = []
        for category, content in categorized_inputs.items():
            if not content:
                continue
                
            if category in self.agents:
                agent = self.agents[category]
                prompt = agent.get_prompt()
                with SuppressStderr():
                    response = invoke_agent(content, weather_text, prompt, category, agent)
                if response:
                    responses.append(response)
            elif content:  # Default to search for unknown categories
                agent = self.agents["Search"]
                prompt = agent.get_prompt()
                with SuppressStderr():
                    response = invoke_agent(content, weather_text, prompt, "Search", agent)
                if response:
                    responses.append(response)
        
        return responses


def main():
    """Main function for testing."""
    orchestrator = AgentOrchestrator()
    
    test_input = (
        "I am feeling energetic today, I want to do a good workout that includes going "
        "to the swimming pool due to it being very hot today, "
        "also add to my training biking and "
        "tell me a good place to do it. I need to eat to boost my protein intake and remind me to drink water in 1 hour"
    )
    
    location = {'lat': 48.8566, 'lon': 2.3522}  # Paris
    orchestrator.process_request(test_input, location)


if __name__ == '__main__':
    main()
