from numbers import Real


def _validate_number(value, arg_name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{arg_name} must be int or float")


def add(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b
