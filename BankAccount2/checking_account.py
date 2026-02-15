# Johnny Chen
# CheckingAccount subclass - inherits from BankAccount

from bank_account import BankAccount


class CheckingAccount(BankAccount):
    """Checking account with transfer/withdrawal limitations."""
    
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit=3):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit  # Maximum number of transfers per month
        self.transfers_made = 0  # Track transfers made this month

    def withdraw(self, amount):
        """Override withdraw to include transfer limitation."""
        if self.transfers_made >= self.transfer_limit:
            print(f"Transfer limit reached! You have made {self.transfers_made}/{self.transfer_limit} transfers this month.")
            return False
        
        # Call parent withdraw method
        if super().withdraw(amount):
            self.transfers_made += 1
            print(f"Transfers remaining this month: {self.transfer_limit - self.transfers_made}")
            return True
        return False

    def transfer(self, amount, recipient_account):
        """Transfer money to another account."""
        if self.transfers_made >= self.transfer_limit:
            print(f"Transfer limit reached! You have made {self.transfers_made}/{self.transfer_limit} transfers this month.")
            return False
        
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot transfer ${amount}. Balance would fall below minimum of ${self.minimum_balance}")
            return False
        
        self.current_balance -= amount
        self.transfers_made += 1
        print(f"Transferred ${amount} to account {recipient_account}")
        print(f"New balance: ${self.current_balance}")
        print(f"Transfers remaining this month: {self.transfer_limit - self.transfers_made}")
        return True

    def reset_transfer_count(self):
        """Reset transfer count (call this at the start of a new month)."""
        self.transfers_made = 0
        print("Transfer count reset for new month.")

    def print_customer_information(self):
        """Override to include transfer limit information."""
        super().print_customer_information()
        print(f"Transfer limit: {self.transfer_limit} per month")
        print(f"Transfers made this month: {self.transfers_made}")
