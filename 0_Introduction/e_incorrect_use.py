"""
Pytype checks the code for statically detectable typing errors. Here, adding a string to an int.
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"


def get_alert_message_2(error_message, team_id):
    return error_message + "- <!" + team_id + ">"


if __name__ == "__main__":
    print(get_alert_message_2("Error", "1"))
    print(get_alert_message_2("Error", 1))  # Flagged
