class BankAccount:
    def __init__(self,AccountHolder,balance):
        self.AccountHolder=AccountHolder
        self.balance=balance

class SavingAccount(BankAccount):
    def __init__(self,AccountHolder,balance,interestRate):
        super().__init__(AccountHolder,balance)
        self.interestRate=interestRate
    def cc(self):
        interestRate=self.balance*self.interestRate/100
        finalbalance=self.balance+interestRate
        print("AccountHolder:",self.AccountHolder)
        print("balance:",self.balance)
        print("interestRate:",interestRate)
        print("finalbalance",finalbalance)
aa=SavingAccount("Shivam",1000,10)
aa.cc()        
    
                
        
        