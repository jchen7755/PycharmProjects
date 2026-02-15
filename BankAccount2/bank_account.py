# Johnny Chen
# Base BankAccount class

class BankAccount:
    bank_title = "Python Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

    def deposit(self, amount):
        """Deposit money into the account."""
        self.current_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.current_balance}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount}. Balance would fall below minimum of ${self.minimum_balance}")
            return False
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")
            return True

    def get_account_number(self):
        """Getter for protected account number."""
        return self._account_number

    def get_routing_number(self):
        """Getter for private routing number."""
        return self.__routing_number

    def print_customer_information(self):
        """Print customer account information."""
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer name: {self.customer_name}")
        print(f"Account number: {self._account_number}")
        print(f"Current balance: ${self.current_balance}")
        print(f"Minimum balance: ${self.minimum_balance}")
