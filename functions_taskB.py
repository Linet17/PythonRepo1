# TASK 1:
# Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
# Hint: Use input () to get the persons input

# def inputString(a):
#     # a = input("Enter string here: ")
#     if a=="yes" or "YES" or "Yes":
#         print("Yes")
#     else:
#         print("No")
# inputString("yes")

# TASK 2:
# Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max () function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.

# def largerThan(a,b,c):
#     a = eval(input("Enter first number here: "))
#     b = eval(input("Enter second number here: "))
#     c = eval(input("Enter third number here: "))
#     if a>b and c:
#         print("{} is greater".format(a))
#         elif b > a and a > c:
#             print ("{} is greater".format(b))
#         elif c>a and c> b:
#         print ("{} is greater".format(c))
#         else:
#         print("None is greater")
# largerThan()

# TASK 3:
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first
# and last elements of the given list. For practice, write this code inside a function

# def listTransformation(a):
#
#     # a.pop[0:8]
#     # x = print(a)
#     new_list = []
#     new_list.append(a[0])
#     new_list.append(a[-1])
#     print(new_list)
#
# a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# listTransformation(a)

# TASK 4:************
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# def evenOddNumber():
#     num = 0
#     if num % 2 == 0:
#         print("{} is an even number".format(num))
#     else:
#         print("{} is an odd number".format(num))
#
#  a = eval(input("Enter first number here: "))
# evenOddNumber(a)

# Extras:
# If the number is a multiple of 4, print out a different message.


# TASK 5:
# With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half
# values in one line and the last half values in one line.

# def tupleTransformation ():
#     tupleList = (list(newTuple))
#     print(tupleList[0:6])
#     print(tupleList[5:11])
#
# newTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tupleTransformation()
