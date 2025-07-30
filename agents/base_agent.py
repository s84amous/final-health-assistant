from abc import ABC, abstractmethod
from smolagents import CodeAgent, LiteLLMModel
from config.settings import MODEL_ID


class BaseAgent(ABC):
    """Base class for all agents."""
    
    def __init__(self, tools=None, max_steps=2, verbosity_level=-1):
        self.model = LiteLLMModel(model_id=MODEL_ID)
        self.tools = tools or []
        self.agent = CodeAgent(
            model=self.model,
            tools=self.tools,
            max_steps=max_steps,
            verbosity_level=verbosity_level
        )
    
    @abstractmethod
    def get_prompt(self) -> str:
        """Return the agent's system prompt."""
        pass
    
    def run(self, input_text: str) -> str:
        """Run the agent with the given input."""
        return self.agent.run(input_text) # pyright: ignore[reportReturnType]
