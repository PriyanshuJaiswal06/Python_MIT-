# where = input("Go left or right? ")
# counter = 0
# while where == "right":
#     counter += 1
#     print(counter)
#     where = input("Go left or right? ") 
    
#     if counter >= 2 and counter<5:
#         print("😑")
#     elif counter >= 5:
#         print("🙄")
#     else:
#         None
# print("You got out! ")
# print("😒")

# Code to find the factorial of any number
# n = int(input("Enter your number: "))
# i = n 
# factorial = 1
# while i > 1:
#     factorial *= i
#     i -= 1
# print(f"The factorial of {n} is {factorial}.")


# #Code to find the factorial of any number (method #2)
# n = int(input("Enter your number: "))
# i = 1 
# factorial = 1
# while n>= i:
#     factorial *= i
#     i += 1
# print("The factorial of {} is {}.".format(n,factorial))

# #Code to find the factorial of any number method #3
# n = int(input("Enter your number: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)
# if we move the print statement in the loop,
# we will be able to find the factorial of number in the range of 1 to n.




#Code to find factorial from range 1 to n:
# n = 10
# i = 1 
# factorial = 1
# while n>= i:
#     factorial *= i
#     i += 1
#     print(f"The factorial of {n} is {factorial}.")

#Code to find factorial from range 1 to n: method #2
# n = int(input("Enter your number: "))
# i = 1 
# factorial = 1
# while n>= i:
#     factorial *= i
#     i += 1
#     print("The factorial of {} is {}.".format(n,factorial))
# n -= 1

#Range
# It generates a sequence of ints, following a pattern
#  range(start, stop, steps)
#  start: first int genetated
#  stop: control last int genearated (go up to but not including this value)
#  steps: used to generate next int in sequence
# It is somewhat similar to slicing
# Ex:
# for i in range(5):
#     print(i)
# for i in range(1,10):
#     print(i)
# for a in range(1,10,2):
#     print(a)
# for j in range(1,4,2):
#     print(j*2)
# for me in range(4,0,-1):
#     print("$"*me)
    
# mysum = 0
# for i in range(10,0,-1):
#     mysum += i
# print(mysum)
    
mysum = 0
start = 3
end = 5
for i in range(start, end + 1 ):
    mysum += i
print(mysum)