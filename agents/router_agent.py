from .base_agent import BaseAgent
from config.settings import CATEGORY_DESCRIPTIONS


class RouterAgent(BaseAgent):
    """Agent for routing user inputs to appropriate specialized agents."""
    
    def __init__(self):
        super().__init__(tools=[], max_steps=3)
    
    def get_prompt(self) -> str:
        """Return the router agent's prompt."""
        desc_lines = "\n".join(f"{cat}: {desc}" for cat, desc in CATEGORY_DESCRIPTIONS.items())
        
        return f"""
You are a classification assistant. Your ONLY task is to analyze user's paragraph then split it into parts then categorize them based on the categories provided using their description.
CATEGORIES:
{desc_lines}

Instructions:
1) Read the full paragraph, analyze it and split it all into parts.
2) For each part, decide which category (or multiple) it belongs to based on intent and your understanding from the predefined CATEGORIES making sure they fit the descriptions provided.
3) If a part does not fit any of the predefined CATEGORIES, then put it as UNKNOWN category.
4) DO NOT provide answers, suggestions, extra commentary, or explanations.
5) DO NOT return anything except classified part under each category name as the OUTPUT FORMAT.
6) Make sure all the input text was split properly and classified, so nothing is missing from the input

OUTPUT FORMAT:
category_name:
- [Sentence].
"""