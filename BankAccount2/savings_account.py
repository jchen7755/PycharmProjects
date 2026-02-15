# Johnny Chen
# SavingsAccount subclass - inherits from BankAccount

from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """Savings account with interest rate."""
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate  # Annual interest rate (e.g., 0.02 for 2%)

    def apply_interest(self):
        """Apply interest to the current balance."""
        interest_earned = self.current_balance * self.interest_rate
        self.current_balance += interest_earned
        print(f"Interest applied: ${interest_earned:.2f}")
        print(f"New balance after interest: ${self.current_balance:.2f}")

    def print_customer_information(self):
        """Override to include interest rate information."""
        super().print_customer_information()
        print(f"Interest rate: {self.interest_rate * 100}%")
