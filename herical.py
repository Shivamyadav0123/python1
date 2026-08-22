class parend:
 def s(self):
     print("This is parend class")

class child1(parend):
   pass        

class child2(parend):
   pass

ss=child1()
s2=child2()
ss.s()
s2.s()