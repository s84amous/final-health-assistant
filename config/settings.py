import os

# API Keys
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "6a3d236035382c8873d5ea8d33a72440")
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY", "f2f6b1736b0e488d9bf536af6b017519")
REMINDERS_API_KEY = os.getenv("REMINDERS_API_KEY", "vCulKBidqDF0MwUza6GSL5kTWwpj66hb6rWmGxYS")

# API URLs
SPOONACULAR_BASE_URL = "https://api.spoonacular.com"
REMINDERS_API_URL = "https://reminders-api.com/api/applications/1231/reminders/"

# Categories
CATEGORIES = ['Weather', 'Fitness', 'Wellbeing', 'Sleep', 'Calendar', 'Nutrition', 'Reminder', 'Search', 'Unknown']

CATEGORY_DESCRIPTIONS = {
    "Weather": "query include weather-related intent",
    "Fitness": "query asks about exercise or fitness routines",
    "Wellbeing": "query shares emotional, mood, or journal-related inputs but not general questions",
    "Sleep": "query talks about sleep, fatigue, or rest",
    "Calendar": "query refers to appointments or events",
    "Nutrition": "query include meal names",
    "Reminder": "query include intent with reminding something",
    "Search": "query include a question but it is not related to the other categories",#  as long as it is not related to weather, fitness, wellbeing, sleep, calender, nutrition, nor reminder",
}

# Model Configuration
MODEL_ID = "ollama/qwen2.5-coder:3b"
