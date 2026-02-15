# Johnny Chen
# Main program - BankAccount Part 2

from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    print("=" * 60)
    print("WELCOME TO PYTHON BANK - Account Management System")
    print("=" * 60)
    
    # ===== SCENARIO 1: Savings Accounts =====
    print("\n" + "=" * 60)
    print("SCENARIO 1: SAVINGS ACCOUNTS")
    print("=" * 60)
    
    # Create first savings account
    print("\n--- Creating Savings Account 1 for Alice ---")
    savings1 = SavingsAccount(
        customer_name="Alice Johnson",
        current_balance=5000,
        minimum_balance=500,
        account_number="SAV-001234",
        routing_number="123456789",
        interest_rate=0.03  # 3% annual interest
    )
    savings1.print_customer_information()
    
    print("\n--- Alice's Transactions ---")
    savings1.deposit(1000)
    savings1.withdraw(500)
    savings1.apply_interest()
    
    # Create second savings account
    print("\n--- Creating Savings Account 2 for Bob ---")
    savings2 = SavingsAccount(
        customer_name="Bob Smith",
        current_balance=10000,
        minimum_balance=1000,
        account_number="SAV-005678",
        routing_number="123456789",
        interest_rate=0.025  # 2.5% annual interest
    )
    savings2.print_customer_information()
    
    print("\n--- Bob's Transactions ---")
    savings2.deposit(2000)
    savings2.apply_interest()
    savings2.withdraw(3000)
    
    # ===== SCENARIO 2: Checking Accounts =====
    print("\n" + "=" * 60)
    print("SCENARIO 2: CHECKING ACCOUNTS WITH TRANSFER LIMITS")
    print("=" * 60)
    
    # Create first checking account
    print("\n--- Creating Checking Account 1 for Charlie ---")
    checking1 = CheckingAccount(
        customer_name="Charlie Brown",
        current_balance=2000,
        minimum_balance=100,
        account_number="CHK-111222",
        routing_number="123456789",
        transfer_limit=3
    )
    checking1.print_customer_information()
    
    print("\n--- Charlie's Transactions ---")
    checking1.deposit(500)
    checking1.withdraw(200)  # Transfer 1
    checking1.withdraw(100)  # Transfer 2
    checking1.transfer(150, "CHK-999888")  # Transfer 3
    checking1.withdraw(50)   # Should fail - limit reached
    
    # Create second checking account
    print("\n--- Creating Checking Account 2 for Diana ---")
    checking2 = CheckingAccount(
        customer_name="Diana Prince",
        current_balance=3000,
        minimum_balance=200,
        account_number="CHK-333444",
        routing_number="123456789",
        transfer_limit=5
    )
    checking2.print_customer_information()
    
    print("\n--- Diana's Transactions ---")
    checking2.deposit(1000)
    checking2.withdraw(400)  # Transfer 1
    checking2.transfer(500, "CHK-777666")  # Transfer 2
    checking2.withdraw(300)  # Transfer 3
    
    # ===== SCENARIO 3: Real-world use case =====
    print("\n" + "=" * 60)
    print("SCENARIO 3: REAL-WORLD USE CASE")
    print("=" * 60)
    
    print("\n--- Emma opens a new checking account and makes transactions ---")
    emma_checking = CheckingAccount(
        customer_name="Emma Watson",
        current_balance=1500,
        minimum_balance=50,
        account_number="CHK-555666",
        routing_number="123456789",
        transfer_limit=4
    )
    
    print("\nEmma checks her account information:")
    emma_checking.print_customer_information()
    
    print("\nEmma deposits her paycheck:")
    emma_checking.deposit(2500)
    
    print("\nEmma pays her rent:")
    emma_checking.withdraw(1200)
    
    print("\nEmma transfers money to her friend:")
    emma_checking.transfer(200, "CHK-888999")
    
    print("\nEmma withdraws cash for groceries:")
    emma_checking.withdraw(150)
    
    print("\nEmma tries to withdraw for entertainment:")
    emma_checking.withdraw(100)  # Should work - 4th transfer
    
    print("\nEmma tries one more withdrawal:")
    emma_checking.withdraw(50)  # Should fail - limit reached
    
    print("\n--- New month begins, Emma's transfer limit resets ---")
    emma_checking.reset_transfer_count()
    
    print("\nEmma can now make transfers again:")
    emma_checking.withdraw(100)  # Should work now
    
    # ===== DEMONSTRATING PROTECTED AND PRIVATE MEMBERS =====
    print("\n" + "=" * 60)
    print("DEMONSTRATING PROTECTED AND PRIVATE MEMBERS")
    print("=" * 60)
    
    print(f"\nAccessing Alice's account number (protected): {savings1.get_account_number()}")
    print(f"Accessing Alice's routing number (private): {savings1.get_routing_number()}")
    
    print("\n" + "=" * 60)
    print("PROGRAM COMPLETED - Thank you for banking with Python Bank!")
    print("=" * 60)


if __name__ == "__main__":
    main()
