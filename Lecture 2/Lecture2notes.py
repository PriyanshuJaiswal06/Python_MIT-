#This lecture is all about string 
#we can concatenate or repeat string 
a = "Priyanshu "
b = "Jaiswal"
name = a + b 
print(name)
a5 = a * 5
print(a5)
#we can find the length of a string using len() operation 
print(len(a))
#first we will do slicing, which is an operation to get the value at certain index in a given string
#the indexing starts with 0
# we can get the last element, or the index of the last element is len(string_name)-1 or just simply -1.
print(a[0])
print(a[-1])
#we can slice string to get a substring using [start:stop:step]
#it will slice from the start index, while including it, to the step-1 index, while taking every step characters.
sliced_a = a[0:9:1]
print(sliced_a)
sliced_b = b[::-1]
#The following is used to reverse any string.
print(sliced_b)
#Examale
s = 'abcdefghijkl'
a = s[2:5]
print(a)
a = s[:]
print(a)
a = s[4:2:-2]
print(a)
#s[:] is same as a[0:len(s):1]
#string are immutable, which means, we cannot modifiy them
#We can create new objects that are versions of the original one.
#variable name can only be bound to one object.
c = "abc"
d = c[0]+"pple"
print(d)
#f-string is a method of printing which is used when we have to print different values of expressions along with literal values, 
#like---
print(f"My name is {name}")
#the output will be,. My name is Priyanshu Jaiswal.
#we place the name of the variable in curly braces.
#Comparision operatiors are used to compare two variable or values,
#they evaluates to boolean values, either True or False
#some conditional operators are:
a = 5
b = 6
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
print(not a)
#logical opeartors on bool:
    #if a and b are two variable with bool values then, 
    # (not a )will return True if the value of a is false and, will return false if a is true.
    # "and" operator return true only when both values are true.
    #"or" operator return true when both or either of them is true
print(a and b)
print(a or b)
#0 is considered as False and all other integer and float is considered as True.
c = 0
d = 1
print(bool(c))
print(bool(d))


