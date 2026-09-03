# lst=[2,3,4,5,6]
# for i in lst:
#     for s in range(1,11):
#         print(i,"*",s,"=",s*i)


#even number
# num=int(input("Enter a number"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")    


# number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for num in number:
#   if num % 2 == 0:
#     print("even number")
#   else:
#     print("odd number") 


# number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for num in number:
#   if num % 2!= 0:
#     print(num)

# s="Shivam yadav"
# for i in s:
#     print(i)


# s = "Shivam yadav"
# print(s[0:6])

# Count=1
# while Count <=5:
#     print("Hello",Count)

#     Count += 1
# print(Count)

# i=2
# while i <=20:
#     print(i)
#     i +=2


# n=int(input("Enter a number:"))
# i=1
# while i <=10:
#     print(n*i)
#     i +=1

# print("Succesfull")  


# n=[1,2,3,4,5,6,7,8,9,10]
# print(n)


# for i in range(2,20,2):
#     print(i)

# num=int(input("Enter a number"))
# for i in range(1,11):
#     print(i*num)


# Python program to check if a number is prime

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
