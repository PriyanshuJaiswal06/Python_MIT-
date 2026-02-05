####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below
# name =  input("Enter your full name: ")
# print(len(name)-5)


####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

# test_string = "We want to remove the nth character from this string"
# n = 8
# a = len(test_string)
# first_half = test_string[:n]
# last_half = test_string[n+1: a]
# # Insert code below
# print(test_string)
# print(first_half + last_half)



####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

# Insert code below

# my_string = "This is my string"  # example string - modify to test
# length = len(my_string)
# if 5>length or length>10:
#     print(True)
# else:
#     print(False)



####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

# Insert code below
count = 0
for i in my_string:
    if i == "e":
        count += 1
print(count)



