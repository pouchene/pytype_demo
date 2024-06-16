"""
"""

def add(a, b):
    return a + b

def add_str():  # Pytype will correctly assign str as output type, despite add being signed Any out
    return add("default", "str")

def add_int():  # Pytype will correctly assign int as output type, despite add being signed Any out
    return add(1, 2)
