# a) Create a function that takes a name and returns a greeting.
def helloName(name):
    print("Hello {}".format(name))

helloName("Linet Gacheri Nyamu")


# b) Write a function that takes the base and height of a triangle and return its area.
def areaOfTriangle(h, b):
    area = int((h * b) / 2)
    print("Area of the triangle is {}".format(area))


areaOfTriangle(10, 30)


# c) Create a function that finds the maximum range of a triangles third edge.
# NOTE: (side1 + side2) - 1 = maximum range of third edge.
# Triangles have side lengths that are positive integers.

def maxRangeOfThirdEdge(side1, side2):
    max = (side1 + side2) - 1
    print("The maximum range of the triangles third edge is {}".format(max))


maxRangeOfThirdEdge(10, 20)


# d)Create a function that takes a list and returns the first element.

def firstListElement():
    print(list1[0])


list1 = [1, 2, 3]
firstListElement()


# e) You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on
# your farm. (CREATE A FUNCTION)

def noOfLegs(chicken, cows, pigs):
    # chickenLegs = 2
    # cowLegs = 4
    # pigLegs = 4
    chickenLegs, cowLegs, pigLegs = 2, 4, 4
    totalChickenLegs = chicken * chickenLegs
    totalCowLegs = cows * cowLegs
    totalPigLegs = pigs * pigLegs
    print("The total number of legs in the firm is {}".format(totalChickenLegs + totalCowLegs + totalPigLegs))


noOfLegs(1, 2, 3)


# f)Create a function that takes a list of numbers. Return the largest number in the list.

# def getMaxNo():
#     listA = []
#     num = int(input("How many numbers do you want to check? : "))
#     for a in range(num):
#         totNumbers = int(input("Enter number: "))
#         listA.append(totNumbers)
#         a += 1
#         print("The largest element in the list is : ", max(listA))
# getMaxNo()

# g) Given a list of integers, return the difference between the largest and smallest integers in the list.
def diffBetweenIntegers():
    print("The difference between the largest and smallest numbers in the list is {}".format(max(listB) - min(listB)))


listB = [10, 20, 40, 50, 78]
diffBetweenIntegers()


# h) Create a function to concatenate two integer lists

def concatenation():
    print("{}".format(listC + listD))


listC = [40, 50, 78]
listD = [90, 80, 70]
concatenation()


# i)Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters
# in the first string is equal to the total number of characters in the second string.
# def stringCharacters():
#     # stringA = ""
#     # stringB = ""
#     if len(stringA) == len(stringB):
#         print(True)
#     else:
#         print(False)
#
#
# # stringA = "I am a working class lady"
# # stringB = "My name is Eric Omondi"
# stringA = input("Enter the first sentence: ")
# stringB = input("Enter the second sentence: ")
# stringCharacters()


# j)Write a function that converts a dictionary into a list, where each element represents a key-value pair.
def dictToList():
    # dictA = {}
    # listE = list(dictA.keys()) + list(dictA.values())
    # listE = dictA.items()
    print(dictA.items())


dictA = {1: 30, 2: 20, 3: 10}
dictToList()

# k)You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
# Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
#Profit = Total Sales - Total Cost
def totalProfit():

    listF = list(dictB.values())
    print(listF)
    profit = round(listF[1] - listF[0],2)
    print(profit)

dictB = {  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200}
totalProfit()
