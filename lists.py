# lists - a collection of more than one variable,like an array.Python does not have arrays.Lists can hold anything including other lists.
# lists are rep by []

personal = []
print = (type(personal))

# personal = ["Linet Nyamu",56,"Nairobi",True,458852.00]
# print(len(personal))

students = ["Dennis", "Linet", "David"]
print(students)
# to print out Dennisli only
print(students[0])
# to slice Dennis out ie print dennis out as a list
print(students[0:1])

# list operations
# to join lists - concatenation
newStudent = ["Jacky"]
allStudents = students + newStudent
print(allStudents)
allStudents.append("Geoffrey")
allStudents.append("Geoffrey")
allStudents.append(" ")
print(allStudents)
# allStudents.clear()

# count
allStudents.count("Geoffrey")
print(allStudents)
# strip- removes spaces outside a string,is a string method
# diff b2n method and function - methods belong to specific classes while functions are independent
# a = "   Savio Muriithi  "
# print(a.index[0])
# print(len("Savio Muriithi"))

# KISS PRINCIPLE - Keep It Stup Simple
# DRY PRINCIPLE - Dont Repeat Yourself

# position = allStudents.index("Jacky")
print(allStudents.index("Jacky"))
print(allStudents)
print(allStudents[1:3])

# insert - an element in a specific position
allStudents.insert(0, "Kassim")
print(allStudents)
allStudents.pop(1)
print(allStudents)
