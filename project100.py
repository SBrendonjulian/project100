class Atm(object):
    def __init__(self,acno,pin,balance):
        self.acno=acno
        self.pin=pin
        self.balance=balance
    def withdraw(self):
        print("withdrawed")
    def deposit(self):
        print("amount deposited")

brendon=Atm(5000,1234,6500)

print(brendon.pin)