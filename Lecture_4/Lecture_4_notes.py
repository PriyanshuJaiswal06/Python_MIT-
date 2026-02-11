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

# using string 
# s = (input("Enter your word: ")).lower()
# alphabet = "" 
# count = 0
# for i in s:
#     if i  not in alphabet:
#         alphabet = alphabet + i
#         count += 1
# print(count)
        

# #Using list 
# s = (input("Enter your word: ")).lower()
# unique = []
# for i in s:
#     if i not in unique:
#         unique.append(i)
# print(len(unique))   


#Guess and check method to find the square root of perfect square number with the help of while loop:
# guess = 0
# x = int(input("Enter the value of x: "))
# if x<0:
#     print(f"Did you mean {-x}????")

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

# num = 17
# #found = False
# for i in range(1,11):
#     if i == num:
#         print(i)
# else:
#     print("guess is out of range.")


#GUESS-and-CHECK CUBE ROOT:POSITIVE CUBES using while loop
# guess = 0 
# x = int(input("Enter your number: "))
# while guess**3<x:
#     guess += 1
# if guess**3 == x:
#     print(f"{guess} is the cube root of {x}.")
# else:
#     print(f"{x} isn't a perfect cube number.")

#GUESS-and-CHECK CUBE ROOT:POSITIVE CUBES using for loop

# x = int(input("Enter your number: "))
# abs_x = abs(x)
# flag = False
# # if x<0:
    
# for i in range(abs_x +1):
#     if i**3 == abs_x :
#         if x<0:
#             print(f"{-i} is the cube root of {x}.")
#         else:
#             print(f"{i} is the cube root of {x}.")
#         break
# else:
#     print(f"{x} isn't a perfect cube number.")


# Remember those word problems from your childhood?
#  For example:
#  Alyssa, Ben, and Cindy are selling tickets to a fundraiser
#  Ben sells 2 fewer than Alyssa
#  Cindy sells twice as many as Alyssa
#  10 total tickets were sold by the three people
#  How many did Alyssa sell?
#  Could solve this algebraically, but we can also use guess-and-check


# total = 10
# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             if ben == alyssa - 2 and cindy == 2*alyssa and alyssa + ben + cindy == total:
#                 print(f"Alysaa sold {alyssa} tickets.")
#                 print(f"Ben sold {ben} tickets.")
#                 print(f"Cindy sold {cindy} tickets.")
                

# Alyssa, Ben, and Cindy are selling tickets to a fundraiser
#  Ben sells 20 fewer than Alyssa
#  Cindy sells twice as many as Alyssa
#  1000 total tickets were sold by the three people
#  How many did Alyssa sell?
       

#Effective method #1 (by myself)          
# for alyssa in range(1000):
#     if (2*alyssa + alyssa- 20 + alyssa) == 1000:
#         print(alyssa)
#         print(2*alyssa)
#         print(alyssa-20)
        
# #Effective method #1 (by professor)              
# for alyssa in range(1001):
#     ben = max(alyssa-20, 0)
#     cindy = 2*alyssa
#     if alyssa + cindy + ben == 1000:
#         print(f"Alyssa sold {alyssa} tickets.")
#         print(f"Ben sold {ben} tickets.")
#         print(f"Cindy sold {cindy} tickets.")


# x = 0 
# for i in range(10):
#     x += 0.1
#     print(x)
# print(10*0.1)
 

#Program to convert decimal digit number into binary digit number
num = int(input())
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False

binary = ""
while num>0:
    binary = str(num%2) + binary
    num = num//2
print(binary)
if is_neg:
    binary = "-" + binary

