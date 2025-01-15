class BankAccount:
    def __init__(self,accountno):
        self.__balance = 0
        self.__acountno=accountno
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"money is deposited and money is {self.__balance}")

    def withdraw(self,amount):
        if(amount>self.__balance):
            print("insufficient balance")
        else:
            self.__balance -= amount
            print(f"money is withdraw and money available is {self.__balance}")
            

    def getbalance(self):
        return self.__balance
    

account=BankAccount("12345")
account.deposit(1000)
account.withdraw(200)
account.getbalance()