#tuples are lists that are immutable ie cannot be changed/manipulated. Used for items youd not want to be changed eg usernames,passwords etc

a = 0 #declaring 'a' as an integer
b = 0.0 #declaring 'a' as a float
c = "" #declaring 'a' as a string
d = [] #declaring 'a' as a list
e = () #declaring 'a' as a tuple


daysofaWeek = ("Mon","Tue","Wed","Thur","Fri","Sat","Sun")
print(type(daysofaWeek))
print(len(daysofaWeek))

#methods include count and index only
daysofaWeek.count("o")
