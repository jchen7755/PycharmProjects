"""
calculator.py
A simple command-line calculator demonstrating clean coding practices.
Supports addition, subtraction, multiplication, division, and modulo.
"""


# ── Arithmetic functions (Single Responsibility + KISS) ──────────────────────

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return a divided by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulo(a: float, b: float) -> float:
    """
    Return the remainder of a divided by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


# ── UI / display functions (Separation of Concerns) ─────────────────────────

OPERATIONS = {
    "1": ("Addition",       add),
    "2": ("Subtraction",    subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division",       divide),
    "5": ("Modulo",         modulo),
}


def display_menu() -> None:
    """Print the list of available operations to the console."""
    print("\n--- Calculator Menu ---")
    for key, (name, _) in OPERATIONS.items():
        print(f"  {key}) {name}")


def get_float(prompt: str) -> float:
    """
    Prompt the user for a floating-point number.
    Keeps asking until valid input is received.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_operation_choice() -> str:
    """
    Prompt the user to choose an operation.
    Keeps asking until a valid menu key is entered.
    """
    while True:
        choice = input("Choose an operation (1-5): ").strip()
        if choice in OPERATIONS:
            return choice
        print("  Invalid choice. Please enter a number between 1 and 5.")


def display_result(operation_name: str, a: float, b: float, result: float) -> None:
    """Print the formatted result of a calculation."""
    print(f"\n  {operation_name}: {a} and {b} → {result}")


# ── Main application loop ────────────────────────────────────────────────────

def run_calculator() -> None:
    """
    Main loop: display menu, collect inputs, perform calculation,
    show result, and ask whether to continue.
    """
    print("Welcome to the Clean Calculator!")

    while True:
        display_menu()

        choice = get_operation_choice()
        operation_name, operation_fn = OPERATIONS[choice]

        a = get_float("Enter the first number:  ")
        b = get_float("Enter the second number: ")

        try:
            result = operation_fn(a, b)
            display_result(operation_name, a, b, result)
        except ValueError as error:
            print(f"  Error: {error}")

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()