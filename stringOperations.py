#concatenation
first_name = "Linet"
last_name = "Nyamu"
full_name = first_name + last_name
print(full_name)
full_name = first_name + " " + last_name
print(full_name)
full_name = "{} {}".format(first_name,last_name)
print(full_name)
print("the tallest person in history is called {} from the family of {}".format(first_name,last_name))

email = "Dear {} Happy Birthday to you daughter {}".format(last_name,first_name)
print(email)

name1 = "Linet Nyamu"
name2 = "kevin murimi"
name3 = "DENNIS SAKAJA"

#name1. calls all methods of string in python
print(name2.capitalize())
print(name3.title())

#count
sen = "man is to error because man didnt create man"
print(sen.count("man"))
sen = "man is to error because Man didnt create man"
print(sen.lower().count("man"))
print(sen.lower().count("a"))

#a string is an iterable
print(sen[0])
print(sen[-1])
#string slicing
#the left most part of the colon signifies the starting element
#right most part of the colon signifies the ending but the final element is excludedq
print(sen[0:2])

jina = "muyani"
print(jina[-3])
print(jina[-6])
print(jina[0:-1])
print(jina[1:4])
print(jina[:])
print(jina[::1])
print(jina[::2])
print(jina[0::])
#inverting/reverting muyani
print(jina[::-1])
print(jina[5::-1])
print(jina[::-2])
print(jina[5:3:-1])

#.split split a string based on the number of spaces
print(sen.split())
#using a letter/character to split a string
print(sen.split("a"))


