"""
You can use functions with different argument types, as long as you don't viuolate annotations.
There are no annotations to violate here.
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"


def get_alert_message_2(error_message, team_id):
    return error_message + "- <!" + team_id + ">"


if __name__ == "__main__":
    print(get_alert_message_1("Error", "1"))
    print(get_alert_message_1("Error", 1))
