"""
"""

def fun_1() -> str:
    var: int
    var = "f"  # Flagged
    return var


def fun_2() -> str:
    var: int = "f"  # Flagged
    return var  # Flagged, using : int annotation and not constant value "f"


def get_str():
    return "f"


def fun_4() -> str:
    var: int
    var = get_str()  # Flagged
    return var


def get_str_annoted() -> str:
    return "f"


def fun_5() -> str:
    var: int
    var = get_str_annoted()  # Flagged
    return var