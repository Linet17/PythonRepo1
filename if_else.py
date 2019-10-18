if True:
    print("True")

marks = input("What was your KCPE marks: ")
#for the input to be accepted as int/float/long etc,use 'eval' function to typecast marks into int or float or long

marks = eval(marks)

# if marks >=350:
#     print("Congratulations,you are admitted")
# else:
#     print("Try again next year")

#nested if
if marks<0 or marks>500:
    print("your marks are unrealistic")
else:
    if marks >= 350 and marks<=500:
        print("Congratulations,you are admitted")
    else:
        print("Sorry,Try again next year")

#read on if-elif-else statements
avg_marks = int(input("Average marks: "))
if avg_marks>80 and avg_marks<=100:
    print("A")
elif avg_marks>=60:
    print("B")
elif avg_marks>=50:
    print("C")
elif avg_marks>=40:
    print("D")
else:
    print("E")

#create an application that identifies if a year is a leap year eg someones birth year