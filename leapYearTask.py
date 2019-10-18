birthYear = int(input("What year were you born?: "))
# print(birthYear%4<1)
# print(birthYear.bit_length())

# if birthYear.bit_length() != 13:
#     print(birthYear, "is not a valid year,please try again.")
# else:

if birthYear % 4 == 0:
    print(birthYear, "is a leap year.")
else:
    print(birthYear, "is not a leap year.")
