# class Number:
#     def __init__(self):
#         self.a=10
#         self.b=20

#     def display(self):
#         print("First number:",self.a)
#         print("Second number:",self.b)

# obj = Number()
# obj.display()     
#       
                

# class aa:
#     def __init__(self):
#        print("Hello I am constructor")

# obj=aa()       


# class aa:
#     def __init__(self,name,branch):
#        self.name=name
#        self.branch=branch
#        print(self.name,self.branch,"this is parents")
# class bb(aa):
#     def __init__(self,name,branch):
#       self.name=name
#       self.branch=branch
     
#       print(self.name,self.branch,"this is child")
#       super().__init__("shubh","cse")
     

             
# c=bb("Sun","CSE")

#single inheritance
class a:
    def cc():
        print("This is child")

class b(a):
    pass
        
oo=b()
b.cc()

#multiple inheritance
class a:
    def cc(self):
        print("This is child")

class d:
    def pp(self):
        print("this is the method of d class")        

class b(a,d):
    pass
        
oo=b()
oo.cc()
oo.pp()


#multi level inheritance

class a:
    def cc(self):
        print("This is child")

class d(a):
    def pp(self):
        print("this is the method of d class")        

class b(d):
    pass
        
oo=b()
oo.cc()
oo.pp()