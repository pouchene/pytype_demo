"""
In the context of this file, the functions are only used with type str in and str out.
Pytype will NOT annotate accordingly. You must write input annotations yourself.
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"


def get_alert_message_2(error_message, team_id):
    return error_message + "- <!" + team_id + ">"


if __name__ == "__main__":
    print(get_alert_message_1("Error", "1"))
    print(get_alert_message_2("Error", "2"))
