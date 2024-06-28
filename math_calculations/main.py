from calculations.basic import add
from calculations.advanced import Calculator
from utils.formatting import format_currency


def main():
    calc = Calculator()
    result = calc.divide(10, 2)
    print("Result of division:", result)

    squared_result = calc.CalculateSquareRoot(-1)

    print("Formatted result:", format_currency(result))


if __name__ == "__main__":
    main()
