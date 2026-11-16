"""A small command-line calculator."""

import sys
from collections.abc import Sequence


def add(first: float, second: float) -> float:
    return first + second


def subtract(first: float, second: float) -> float:
    return first - second


def multiply(first: float, second: float) -> float:
    return first * second


def divide(first: float, second: float) -> float:
    if second == 0:
        raise ValueError("Cannot divide by zero.")
    return first / second


def calculate(operation: str, first: float, second: float) -> float:
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    try:
        calculator_operation = operations[operation]
    except KeyError as error:
        raise ValueError(f"Unknown operation: {operation}") from error
    return calculator_operation(first, second)


def main(arguments: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if arguments is None else arguments)
    if len(arguments) != 3:
        print("Usage: python calculator.py <add|subtract|multiply|divide> <first> <second>")
        return 1

    operation, first_text, second_text = arguments
    try:
        first = float(first_text)
        second = float(second_text)
        result = calculate(operation, first, second)
    except ValueError as error:
        print(f"Error: {error}")
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
