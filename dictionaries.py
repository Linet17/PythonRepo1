personal = ["Linet Nyamu",56,"Nairobi",True,458852.00]

#a dictionary is a data structure that holds 'key' & 'value' or 'property' & 'value'
#can type-cast a dict to list or tuple

a = 0 #defining 'a' as an integer
b = 0.0 #defining 'a' as a float
c = "" #defining 'a' as a string
d = [] #defining 'a' as a list
e = () #defining 'a' as a tuple
f = {} #defining 'a' as a tuple

f = {}
print(type(f))

personal = {"name":"Linet Nyamu",
            "Age": 56,
            "Location":"Nairobi",
            "is_Tall":True,
            "Net-worth":458852.00}

#how to access an element - use a key to access
print(personal["name"])

#methods
#research on .fromkeys() method

print(personal.get("age"))
print(personal.keys("age"))
print(personal.pop("is_Tall"))