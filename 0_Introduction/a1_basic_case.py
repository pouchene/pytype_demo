"""
Pytype checks and infers types for your Python code - without requiring type annotations
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"  # Found to always return a string


def get_alert_message_2(error_message, team_id):
    return error_message + "- <!" + team_id + ">"  # This function should also always return a string... right?
