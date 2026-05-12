"""Simple calculator module used for Jenkins CI/CD Basics demo."""


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers."""
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """Return a divided by b. Raises ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
