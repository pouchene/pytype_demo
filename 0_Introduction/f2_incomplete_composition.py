"""
"""

def add(a, b):
    return a + b

def add_str(a, b) -> str:  # Although add returns Any, default_str will still be typed str out thanks to the annotation.
    return add(a, b)

# You will be prevented from using default_str with anything not resulting in a str, provided pytype can perform the type check.

if __name__ == "__main__":
    print(add_str("a", "b"))  # OK
    print(add_str(1, 2))  # Flagged
