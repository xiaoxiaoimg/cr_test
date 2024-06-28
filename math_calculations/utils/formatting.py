def format_number(number, decimal_places=2):
    """Format a number to a specified number of decimal places."""
    return f"{number:.{decimal_places}f}"


def format_currency(number, currency_symbol="$"):
    """Format a number as currency."""
    return f"{currency_symbol}{format_number(number)}"
