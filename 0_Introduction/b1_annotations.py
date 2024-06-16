"""
If you provide type annotations, they will be used to infer even more.
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"


def get_alert_message_2(error_message: str, team_id: str):  # Extra annotations here allow pytype to detect output type
    return error_message + "- <!" + team_id + ">"
