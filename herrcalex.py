class parend:
    
    def add(self):
        a=int(input("Enter a number"))
        b=int(input("Enter a number"))
        print(a+b)

class child1(parend):
    def sub(self):
        a=10
        b=20
        print(a-b)
        super().add()

class child2(parend):
    def mul(self):
        a=10
        b=20
        print(a*b)
        super().add()
        

ss=child1()
s2=child2()
ss.sub()
s2.mul()                