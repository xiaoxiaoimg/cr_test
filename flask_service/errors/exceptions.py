class ValidationError(Exception):
    pass


def unsafe_eval(input_string):
    return eval(input_string)
