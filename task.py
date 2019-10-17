taskList = [23, "Jane", ["Lesson23", 560, {"Currency": "KES"}], 987, (76, "John")]
# print(taskList)

# 1.Determine the type of variable in taskList using an inbuilt function
print(type(taskList))

# 2.Print Kes
# print(taskList.count("Jane"))
# print(taskList.index(987))

a = "".join(map(str, taskList))
# # a = dict
# a = {a}
print(a)

# print(a.get("Currency"))

# 3.Print 560
# print(a[19:22])
print(taskList[2][1])

# 4.Use a function to determine the length of taskList
# print(a.index("Jane"))
print(len(taskList))

# 5.Change 987 to 789 without using an inbuilt method or assignment
# print(a[44:47:-1])
# print(taskList)
b = str(taskList[3])[::-1]
print(b)
print(str(taskList[3])[::-1])

# 6.Change the name "John" to "Jane" without using assignment
#[] acts as an accessor
# "N/A"
