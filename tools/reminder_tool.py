import re
import requests
from datetime import datetime, timedelta
from smolagents import Tool
from config.settings import REMINDERS_API_KEY, REMINDERS_API_URL


class ReminderTool(Tool):
    """Tool to create reminders via API."""
    
    inputs = {
        "reminder_text": {
            "type": "string",
            "description": "Reminder content to schedule"
        }
    }
    output_type = "string"
    name = "ReminderTool"
    description = "Tool to create a new reminder by sending it to the reminders API."

    def forward(self, reminder_text: str) -> str: # pyright: ignore[reportIncompatibleMethodOverride]
        """Create a reminder from the given text."""
        headers = {
            "Authorization": f"Bearer {REMINDERS_API_KEY}",
            "Content-Type": "application/json"
        }
        
        title = reminder_text.strip().capitalize()
        timezone = "Europe/Paris"
        now = datetime.now()
        
        # Extract date
        date_match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", reminder_text)
        date_str = date_match.group(1) if date_match else (now + timedelta(days=1)).strftime("%Y-%m-%d")

        # Extract time
        time_match = re.search(r"\b(\d{2}:\d{2})\b", reminder_text)
        time_str = time_match.group(1) if time_match else "09:00"
        
        # Extract notification advance
        notify_match = re.search(r"\b(in|before)\s+(\d+\s+(minutes?|hours?|days?|weeks?))", reminder_text, re.IGNORECASE)
        notify_in_advance = notify_match.group(2) if notify_match else "10 minutes"
        
        payload = {
            "title": title,
            "timezone": timezone,
            "date_tz": date_str,
            "time_tz": time_str,
            "notify_in_advance": notify_in_advance,
            "snoozed": 0
        }
        
        try:
            response = requests.post(REMINDERS_API_URL, headers=headers, json=payload)
            response.raise_for_status()
            return f"Reminder created for {date_str} at {time_str}: {title}"
        except Exception as e:
            return f"Failed to create reminder: {e}"