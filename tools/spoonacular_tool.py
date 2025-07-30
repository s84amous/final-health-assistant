import requests
from smolagents import Tool
from config.settings import SPOONACULAR_API_KEY, SPOONACULAR_BASE_URL


class SpoonacularTool(Tool):
    """Tool for searching recipes and getting nutritional information."""
    
    inputs = {
        "input_text": {
            "type": "string",
            "description": "Command: 'search:<query>' or 'details:<id>'"
        }
    }
    output_type = "string"
    name = "SpoonacularTool"
    description = "Use this tool to search recipes or fetch full details: instructions, nutrition, taste"

    def forward(self, input_text: str) -> str: # pyright: ignore[reportIncompatibleMethodOverride]
        """Process the input command."""
        command, _, arg = input_text.partition(":")
        
        if command == "search":
            return self._search_recipes(arg)
        elif command == "details":
            return self._get_nutritional_info(arg)
        else:
            return f"Unknown command: {input_text}"

    def _search_recipes(self, query: str, number: int = 1) -> str:
        """Search for recipes."""
        url = f"{SPOONACULAR_BASE_URL}/recipes/complexSearch"
        params = {
            'query': query,
            'number': number,
            'addRecipeInformation': False,
            'apiKey': SPOONACULAR_API_KEY
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json().get('results', [])
            return "\n".join(f"{r['id']}: {r['title']}" for r in results)
        except Exception as e:
            return f"Error searching recipes: {e}"

    def _get_nutritional_info(self, recipe_id: str) -> str:
        """Get nutritional information for a recipe."""
        try:
            response = requests.get(
                f"{SPOONACULAR_BASE_URL}/recipes/{recipe_id}/nutritionWidget.json",
                params={'apiKey': SPOONACULAR_API_KEY}
            )
            response.raise_for_status()
            nutrition = response.json()
            
            output = "**Instructions:**\n"
            output += "\n**Nutrition per serving:**\n"
            output += f"- Calories: {nutrition['calories']}\n"
            output += f"- Carbs: {nutrition['carbs']}\n"
            output += f"- Fat: {nutrition['fat']}\n"
            output += f"- Protein: {nutrition['protein']}\n\n"
            output += "**Taste Profile:**\n"
            
            return output
        except Exception as e:
            return f"Error getting nutritional info: {e}"
