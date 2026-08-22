class parent:
  def show_parent(self):
    print("This is parant class")

class child(parent):
    def show_child(self):
     print("This is child class")

obj=child()         
obj.show_parent()
obj.show_child()



class father:
  def father(self):
    print("this is father class")

class mather:
  def mather(self):
    print("this is mather class")


class child( father , mather):
  def child(self):
    print("this is child class")        



obj=child()
obj.father()
obj.matther()
obj.child()   



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