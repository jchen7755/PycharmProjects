# Assignment 2 - Modular Sandwich Maker Machine

This project is a modular version of the Ham Sandwich Maker Machine from Assignment 1. The code has been split into four separate files for better organization and maintainability.

## Project Structure

```
Assignment2/
├── main.py              # Main entry point of the program
├── sandwich_maker.py    # SandwichMaker class - handles sandwich making
├── cashier.py          # Cashier class - handles payment processing
└── data.py             # Data storage - recipes and resources
```

## File Descriptions

### main.py
- Acts as the starting point of execution for the program
- Imports all necessary modules
- Creates instances of SandwichMaker and Cashier classes
- Contains the main loop that handles user input

### sandwich_maker.py
- Contains the `SandwichMaker` class
- `check_resources()` - Checks if sufficient ingredients are available
- `make_sandwich()` - Deducts ingredients and makes the sandwich

### cashier.py
- Contains the `Cashier` class
- `process_coins()` - Accepts coin input and calculates total payment
- `transaction_result()` - Validates payment and returns change if needed

### data.py
- Stores the recipes dictionary (small, medium, large sandwiches)
- Stores the resources dictionary (available ingredients)
- Acts as a database for the program

## How to Run

```bash
python main.py
```

## Usage

When you run the program, you can:
- Order a sandwich: Type `small`, `medium`, or `large`
- Check resources: Type `report`
- Turn off machine: Type `off`

## Example Interaction

```
What would you like? (small/ medium/ large/ off/ report): small
Please insert coins.
how many large dollars?: 2
how many half dollars?: 0
how many quarters?: 0
how many nickels?: 0
Here is $0.25 in change.
Small sandwich is ready. Bon appetit!
```

## Requirements

- Python 3.x
- No external libraries required
