"""
Pytype checks and infers types for your Python code - without requiring type annotations
"""

def get_alert_message_1(error_message, team_id):
    return f"{error_message} - <!{team_id}>"  # Found to always return a string


def get_alert_message_2(error_message, team_id):
    return error_message + "- <!" + team_id + ">"  # This function should also always return a string... right?


# We CAN create a class, for which adding a string to it does absolutely nothing
class CannibalString(object):
    def __init__(self, value: str) -> None:
        self.value = value

    def __add__(self, other):
        if  isinstance(other, CannibalString):
            return CannibalString(self.value + other.value)
        if isinstance(other, str):
            return self
    
    def __str__(self):
        return self.value


if __name__ == "__main__":
    print(get_alert_message_2("Error", "1"))
    print(get_alert_message_2(CannibalString("Error"), CannibalString("1")))
