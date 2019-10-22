# repeating yourself
my_name = "Daniel Kabiru"

print(my_name)

# while loops
a = 0
while a < 100:
    print("{}. {}".format(a + 1, my_name))
    a += 1

# a while loop repeats execution of its indented code/ block until a condition is false
saved_pin = "9999"

tries = 3
current_pin = input("Enter Pin: ")
print("That was attempt {}".format(4 - tries))
tries -= 1
while current_pin != saved_pin and tries > 0:
    current_pin = input("Try Again: ")
    tries -= 1
    print("That was attempt {}".format(3 - tries))

if current_pin != saved_pin:
    print("card blocked")
else:
    print("Success, Welcome!!")
    # if attempt <= 3:
    #     current_pin = input("Try Again: ")
    #     attempt += 1
    #     print("That was attempt {}".format(attempt))
    # else:
    #     print("Sorry you have exhausted attempts")
    #     break

# for loops
