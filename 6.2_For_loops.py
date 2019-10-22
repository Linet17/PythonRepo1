# For loops
# a for loop loops over a given range
# the i in the example represents each individual member of the range
# in range the last value is excluded

for i in range(10):  # this range starts at zero and ends at 9
    print(i + 1)

for num in range(5, 10):  # this range starts at 5 and ends at 9
    print(num)
#
for num in range(5, 20, 2):  # this range starts at 5 and ends at 19 at intervals (steps) of 2
    print(num)

house = {"utensils": ["spoon", "fork", "plates", "cup"],
         "clothes": ["beddings", "jacket", "umbrella", "raincoat"]}
#
for each in house:
    print(house[each])
    for i in house[each]:
        print(i)

students = ['ali', 'kasim', 'andrew', 'eugene']

for student in students:
    student += " Kamau"
    print(student)

subjects = [23, 45, 67, 89, 56]

total = 0
for each in subjects:
    total = + each
print(total)

# Question
# write a program that prints your name 100 times using a while and a for loop

# ***** ASSIGNMENT******** #
# write a for loop that output 8,11,14,17,20, upto 83, 86,89

for e in range(8, 90, 3):
    print(e)

#first 20 numbers and their squares and cube use for loop and While loop
for no in range(21):
    square = no ** 2
    cube = no ** 3
    print("{} ...{} ...{}".format(no, square, cube))

number = 1
while number <= 20:
    square = number ** 2
    cube = number ** 3
    print("{} ...{} ...{}".format(number, square, cube))
    number += 1
