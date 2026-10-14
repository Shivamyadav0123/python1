a=[2,3]
for i in a:
    print("Table",i)
    for s in range(1,11):
        print(i,"*",s,"=",i*s)

a=int(input("Enter a number"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)    