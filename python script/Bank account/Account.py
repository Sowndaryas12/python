class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1

    @classmethod
    def display_total_accounts(cls):
        print(f"Total bank accounts: {cls.total_accounts}")
        

    