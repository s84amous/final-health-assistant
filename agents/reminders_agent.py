"""Reminder agent for creating and managing reminders."""
from .base_agent import BaseAgent
from tools.reminder_tool import ReminderTool


class ReminderAgent(BaseAgent):
    """Agent for creating and managing reminders."""
    
    def __init__(self):
        super().__init__(tools=[ReminderTool()])
    
    def get_prompt(self) -> str:
        """Return the reminder agent's prompt."""
        return """
IMPORTANT: This is a reminder-related query. You must create and schedule a reminder using the provided content. Extract and structure the information accurately.

You must determine and prepare the following fields:
- Title: A clear, concise description of what the reminder is for.
- Date (date_tz): The local date when the reminder should trigger. Use YYYY-MM-DD format. If not specified, default to tomorrow.
- Time (time_tz): The local time when the reminder should trigger. Use HH:MM format. If not specified, default to 09:00.
- Timezone: Use "Europe/Helsinki" unless another timezone is clearly specified.
- Notify in Advance (notify_in_advance): How much earlier the user should be notified. Accept formats like "10 minutes", "1 hour", or "2 days". If unspecified, default to "10 minutes".
- Optional Recurrence (rrule): Include only if user mentions repeating, recurring, or scheduling something regularly.
- Optional Snoozed (snoozed): Set to 1 if user explicitly says to pause, snooze, or delay the reminder.

Use this information to call the ReminderTool with the correct structure.

Only return the final confirmation message:
- Confirm the reminder was scheduled
- Mention the title, date, time, and advance notification

Do not show code or tool calls. Do not explain your process. If unable to create the reminder, return "NO_RESPONSE".
"""