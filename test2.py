# a = int(input("Enter a number: "))

# if a > 1:
#      for i in range(2, int(a ** 0.5) + 1):
#          if a % i == 0:

#              print(a, "is not a prime number")
#              break
#      else:
#          print(a, "is a prime number")
# else:
#      print(a, "is not a prime number")



#Create a class named Student with the attributes name, roll number, and marks. Create two
#objects and display the details of both students using a class method.


# class Student:
#      def __init__(self, name, roll_number, marks):
#          self.name = name
#          self.roll_number = roll_number
#          self.marks = marks

#      def d(self):
#          print("Name:", self.name)
#          print("Roll Number:", self.roll_number)
#          print("Marks:", self.marks)


# student1 = Student("Rahul", 101, 85)
# student2 = Student("Priya", 102, 92)
# student1.d()
# student2.d()

#2

# num = int(input("Enter a number: "))
# def factorial(n):
#     result = 1

#     for i in range(1, n + 1):
#         result *= i

#     return result

# print("Factorial of", num, "is", factorial(num))



# class P:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(P):
#     def __init__(self, name, age, roll_number, course):
#         super().__init__(name, age)
#         self.roll_number = roll_number
#         self.course = course


# student = Student("Rahul", 20, 101, "BCA")
# print("Name:", student.name)
# print("Age:", student.age)
# print("Roll Number:", student.roll_number)
# print("Course:", student.course)



#Write a Python program that accepts a list of numbers and finds the second largest number without
#using the sort() function.

#lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#if


#8. Set Operations
#Create two sets of student names. Write a program to display the students who are common in both
#sets, students who are only in the first set, and students who are only in the second set.


# set1={"Shubh","Shivam","devansh","anand","Ram"}
# set2={"Shubh","Abhishek","Aman","Shivam","Ram"}

# # common=set1 & set2
# # print("common name",common)

# # def calculate_numbers(numbers):
# #     total = sum(numbers)
# #     average = total / len(numbers)
# #     largest = max(numbers)
# #     smallest = min(numbers)

# #     print("Sum:", total)
# #     print("Average:", average)
# #     print("Largest:", largest)
# #     print("Smallest:", smallest)

#  numbers = [10, 20, 5, 30, 15]
#  calculate_numbers(numbers)


#5

#lst=[10,11,12,13,14,15,16,17,18,19,20]


for i in range(2,100,2):
    print(i)
 



