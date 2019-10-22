# For Loops

# stationery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# stationery = ["Pencils","Rubbers","Rulers","Books"]
# print=(type(stationery))

# using for loops for dictionaries
# house = {"utensils": ["spoon", "fork", "plates", "cup"],
#          "clothes": ["beddings", "jacket", "umbrella", "raincoat"]}
# for each in house:
#     print(house[each])  # prints out the lists in the dictionary as they are
# for i in house[each]:
#     print(i)

# using for loops with lists
utensils = ["spoon", "fork", "plates", "cup"]
for a in utensils:
    print(a)

# using for loops with tuple
clothes = ("beddings", "jacket", "umbrella", "raincoat")
for b in clothes:
    print(b)

names = [" Linet Nyamu", " Anthony Nyamu", " Morris Nyamu", " Lydia Nyamu"]
for each in names:
    names.remove("Nyamu")
    print(names)
    # names.strip()
    # print(names)
