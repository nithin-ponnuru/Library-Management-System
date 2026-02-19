# bank account class
'''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ₹{amount}"
        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        elif amount <= 0:
            return "Withdrawal amount must be positive"
        else:
            self.balance -= amount
            return f"Withdrew: ₹{amount}"

    def get_balance(self):
        return f"Current balance: ₹{self.balance}"
account = BankAccount("Mohan", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())'''


class IPPB_Account:
    def __init__(self, name="Nithin", acc_no=123456, pin=2005, balance=0):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance

    def pinvalidation(self):
        attempts = 1
        while attempts <= 3:
            atmpin = int(input("\nEnter 4-Digit ATM PIN: "))
            if atmpin < 1000 or atmpin > 9999:
                print("PIN Must be Exactly 4 digits")
                continue
            if atmpin == self.pin:
                print("PIN Verified Successfully")
                break
            else:
                if attempts < 3:
                    print("Wrong PIN. Remaining attempts:", 3 - attempts)
                attempts = attempts + 1
        if attempts > 3:
            print("ATM Card Blocked Due to 3 Wrong Attempts")

account = IPPB_Account()
print(account.pinvalidation())
