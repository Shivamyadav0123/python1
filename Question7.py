from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class Creditcard(Payment):
    def pay(self,amount):
        print("Payment paid by credit card: ",amount)
class UPIPayment(Payment):
    def pay(self,amount):
        print("Payment paid by UPI: ",amount)
class CashPayment(Payment):
    def pay(self,amount):
        print("Payment paid by cash: ",amount)
def pro(payment ,amount):
    payment.pay(amount)
cc=Creditcard()
up=UPIPayment()
ca=CashPayment()
pro(cc,1000)
pro(up,2000)
pro(ca,3000)