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
