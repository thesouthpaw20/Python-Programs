class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}")

class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

def create_account():
    account_type = input("Enter account type (savings/current): ").strip().lower()
    owner = input("Enter account owner name: ")
    balance = float(input("Enter initial balance: "))
    
    if account_type == 'savings':
        account = SavingsAccount(owner, balance)
    elif account_type == 'current':
        account = CurrentAccount(owner, balance)
    else:
        print("Invalid account type. Please enter 'savings' or 'current'.")
        return None
    
    return account

def main():
    accounts = []
    
    while True:
        print("\nSelect operation:")
        print("1. Create a new account")
        print("2. Perform operations on existing accounts")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            account = create_account()
            if account:
                accounts.append(account)
                print(f"Account created for {account.owner}.")
        elif choice == '2':
            if not accounts:
                print("No accounts available. Please create an account first.")
                continue
            
            owner = input("Enter the account owner name: ")
            account = next((acc for acc in accounts if acc.owner == owner), None)
            
            if account is None:
                print(f"No account found for owner: {owner}")
                continue
            
            while True:
                print(f"\nSelect operation for {account.owner}:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                if isinstance(account, SavingsAccount):
                    print("4. Add interest")
                print("5. Back to main menu")
                
                operation = input("Enter choice: ")
                
                if operation == '1':
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                elif operation == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                elif operation == '3':
                    print(f"Current balance: {account.get_balance()}")
                elif operation == '4' and isinstance(account, SavingsAccount):
                    account.add_interest()
                elif operation == '5':
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    main()
