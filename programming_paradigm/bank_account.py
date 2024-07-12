class BankAccount:
    def __init__(self, account_balance = 0):
        """Initializes a BankAccount object with an optional initial balance."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Adds the amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Debits account if funds sufficient, denies withdrawal if otherwise."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            # print("Insufficient funds.")
            return False

    def display_balance(self):
        """Prints the account balance."""
        print(f"Current Balance: ${self.account_balance:2f}")

