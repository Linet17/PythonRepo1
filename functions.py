# # functions are a group of related statements that perfom a specific task
# # uses keyword def
# # syntax -> def functionName():
# # statements
# # exapmle 1
# def helloWorld():
#     print("Hello world")
#
#
# helloWorld()  # to use a function,you need to call it
#
#
# # example 2
# def add_two_numbers():
#     pass  # used when youre not sure what to put in the body yet to help still be able to pass/call the function
#
#
# def addTwoNumbers(a, b):  # a and b are that that'll be expected once the function is called
#     sum = a + b
#     print(sum)  # or print(a+b)
#
#
# addTwoNumbers(10, 10)
# addTwoNumbers(45, 10)
# addTwoNumbers("Linet", "Nyamu")
#
#
# # example 3
# def subTwoNumbers(a, b):
#     print(a - b)
#
#
# subTwoNumbers(10, 10)
# subTwoNumbers(300, 500)

# #
# def greaterThan(num):
#     # num = eval(input("Enter a number: "))
#     if num > 100:
#         print("{} is great than 100".format(num))
#     else:
#         print("{} is less than 100".format(num))
# greaterThan(50)
#
# def multiply(a,b):
#     # a = 3
#     # b = 9
#     print(a * b)
#
#  multiply(12,10)
#
# def divisibleByTwo(num):
#     # num = eval(input("Enter first number: "))
#     if num%2==0:
#         print("{} is divisible by 2".format(num))
#     else:
#         print("{}".format(num, "is not divisible by 2"))
# divisibleByTwo(205)
#
# def upper_case():
#     name = input("Enter your first name: ")
#     # name = "linet nyamu"
#     print(name.capitalize())
# upper_case()
#
# def upperCaseFirstLetter(name):
#     index1 = name[0].upper()
#     fullName = index1 + name[1:]
#     print(fullName)
# upperCaseFirstLetter("good morning")

# def stringReplace():
#     names = "Good Morning"
#     print(names.replace("Morning","Evening"))
#
# stringReplace()

def addNumbers(a,b):
    return a+b

x = addNumbers(10,10) #allows the results of the function or
print(x)

print(addNumbers(10,10))


