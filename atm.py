class Atm:
   def __init__(self): #constructor(special function)
     self.pin=''
     self.balance=0
     self.menu()


   def menu(self):
    user_input=input("""
     Hi how can I help you?
     1. Press 1 to create pin
     2. Press 2 to change pin
     3. Press 3 to check balance
     4. Press 4 to withdraw
     5. Anything else to exit 
     """)  
    if user_input =="1":
       #create pin
       self.create_pin()
    elif user_input =="2":
       #change pin
       pass
    elif user_input =="3":
       #check balance
       pass
    elif user_input =="4":
       #withdraw
       pass
    else:
      exit()
   def create_pin(self):




     
obj=Atm()
   