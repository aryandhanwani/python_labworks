class balance():
    def __init__(self):
        self.balance=0
    
    def deposit(self):
        amount = int(input("Enter the amount to deposit:"))

        if amount<0:
            print("amount should be positive")
            
        else:
            self.balance+=amount
    
    def withdraw(self):
        amount = int(input("Enter the amount to withdraw:"))

        if amount>0 and amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")
            
    
    def check_balance(self):
        print(f"Current Balance is: {self.balance}")

b=balance()

b.deposit()
b.withdraw()
b.check_balance()
