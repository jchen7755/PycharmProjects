# Johnny Chen

class BankAccount:
    bank_title = "Python Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.current_balance}")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print(f"Cannot withdraw ${amount}. Balance would fall below minimum of ${self.minimum_balance}")
        else:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")

    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer name: {self.customer_name}")
        print(f"Current balance: {self.current_balance}")
        print(f"Minimum balance: {self.minimum_balance}")

print("=== Creating Account 1 ===")
account1 = BankAccount("Alice Johnson", 1000, 100)
account1.print_customer_information()

print("\n=== Testing Account 1 ===")
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1300)  # This should fail - would go below minimum

print("\n=== Creating Account 2 ===")
account2 = BankAccount("Bob Smith", 500, 50)
account2.print_customer_information()

print("\n=== Testing Account 2 ===")
account2.deposit(100)
account2.withdraw(400)
