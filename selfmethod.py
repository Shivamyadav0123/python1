class s:
   def add (self,*args):
        print(sum(args))
obj=s()
obj.add(10,20)
obj.add(10,20,30)      