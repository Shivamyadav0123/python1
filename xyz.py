for i in range(1,100,2):
    print(i)

lst=[2,3,4,5]
for i in lst:
    print(i*i)
#

lst=[1,2,3,4,5,6]
for i in lst:
 if i%2==0:
  print(i)
#
a=4
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)    
#

num= int(input("Enter a number"))
if num<=1:
    print("not prime number")
else:
    for i in range(2,num):
        if num %i ==0:
            print("not prime number")
    
        else:    
         print("not prime number")    



