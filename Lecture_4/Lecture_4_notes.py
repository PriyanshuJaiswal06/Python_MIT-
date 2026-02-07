#Use of break statement to pause a loop after certain condition
# mysum = 0
# for i in range (5, 11, 2):
#     mysum += i
#     if mysum == 14:
#         break
#     mysum += 1
# print (mysum)

# count = 0 
# for i in range(5):
#     if i%2 == 0:
#         count += 1
# print(count)

# count = 0
# for i in range(10):
#     if i%2 == 0:
#         count += 1
# print(count)

# count = 0
# for i in range(2,9,3):
#     if i%2 == 0:
#         count += 1
# print(count)

 
# count = 0
# for i in range(-4,6,2):
#     if i%2 == 0:
#         count += 1
# print(count)

# count = 0
# for i in range(5,6):
#     if i%2 == 0:
#         count += 1
# print(count)

#looping over character in a string:
# s = "Priyanshu Jaiswal"
# a = "l"
# b = "P"
# for index in range(len(s)):
#     if s[index] == "l" or s[index] == "P":
#         print(f"There is a {a} and {b} in this string")
# print(len(s))

# s = "One Piece is Real."
# for char in s:
#     if char == "i":
#         print("There is an i in this string.")
        
        
# for i in s:
#     if i in "il":
#         print("There is an i or l")

#to count number of vowels in a given string        
# s = "jdfslkdhfhdfoweih;vjkfyrfiewrdkjfherliuthf"
# count = 0
# for i in s:
#     if i in "aeiou":
#         count += 1
# print(count)

#Robot Cheerleader
# vowels = "aeiouAEIOU"
# word = input("I'll cheer for you! Enter your word: ")
# times = int(input("Enter your Enthusiam level (1-10): "))
# for w in word:
#     if w in vowels:
#         print(f"Give me an {w} : {w}.")
#     else:
#         print(f"Give me a {w} : {w}.")
# print("What does it spell?")
# for i in range(times):
#     print(word, "!!!")
    
# Assume you are given a string of lowercase letters in variable s.
# Count how many unique letters there are in the string.

#using string 
# s = input("Enter your word: ")
# alphabet = "" 
# count = 0
# for i in s:
#     if i  not in alphabet:
#         alphabet = alphabet + i
#         count += 1
# print(count)
        

# #Using list 
# s = input("Enter your word: ")
# unique = []
# for i in s:
#     if i not in unique:
#         unique.append(i)
# print(len(unique))   


#Guess and check method to find the square root of perfect square number with the help of while loop:
# guess = 0
# x = int(input("Enter the value of x: "))
# if x<0:
#     print(f"Did you really mean {x}????")

# if x>=0:
#     while guess**2 < x:
#         guess += 1
#     if guess**2 == x:
#         print(f"{guess} is the square root of {x}.")
#     else:
#         print(f"{x} is not a perfect square number.")


#Guess and check method to find the square root of perfect square number with the help of for loop:
# x = int(input("Enter the value of x: "))
# till = int(x/2 +1)
# found = False
# for i in range(till):
#     if i**2==x:
#         print(f"{i} is the square root of {x}.")
#         found = True
#         break
# if not found:
#         print(f"{x} is not a perfect square number.")
        

#Try on your own:
# Hardcode a number as a secret number.
# Write a program that checks through all the numbers from 1 to 10 and 
# prints the secret value if it's in that range. If it's not found, 
# it doesn't print anything.


# num = 7
# for i in range(1,11):
#     if i == num:
#         print(i)

# How does the program look if I change the requirement to be If it's not found, 
# prints that it didn't find it.

num = 17
found = False
for i in range(1,11):
    if i == num:
        print(i)
else:
    print("guess is out of range.")



