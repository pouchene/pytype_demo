"""
If you provide type annotations, they must be respected.
"""

def get_alert_message_1(error_message: str, team_id: str):  # Input type with str annotation, any use other than str will be flagged
    return f"{error_message} - <!{team_id}>"


def get_alert_message_2(error_message: str, team_id: str):
    return error_message + "- <!" + team_id + ">"


if __name__ == "__main__":
    print(get_alert_message_1("Error", 1))  # Flagged
