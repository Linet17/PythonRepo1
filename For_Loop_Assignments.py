# write a program that prints your name 100 times using a while and a for loop
# ONLY the range variable declaration comes before for while any other declarations come after
# a = 0
for a in range(101):
    myName = "Linet Nyamu"
    print("{}.{}".format(a, myName))
    print("{} Linet Nyamu".format(a))

# write a for loop that output 8,11,14,17,20, upto 83, 86,89
for b in range(8, 90, 3):
    print(b)

# write a while loop that output 8,11,14,17,20, upto 83, 86,89
a = 8
while 8 <= a <92:
    print(a)
    a+=3


#first 20 numbers and their squares and cube use for loop and While loop
for no in range(1,21):
    square = no ** 2
    cube = no ** 3
    print("{} ...{} ...{}".format(no, square, cube))

number = 1
while number <= 20:
    square = number ** 2
    cube = number ** 3
    print("{} ...{} ...{}".format(number, square, cube))
    number += 1

print(range(0,100))
x = range(0,100)
print(type(x))
print(x)

