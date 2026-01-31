# Write a program that:
# 1. Asks the user for the verb
# 2.prints "I can _ better than you." where you replace _ with the verb.
# then prints the verb 5 times in a row separated by spaces.
#for example, if the user enters RUN, you prints:
# I can run better than you.
# run run run run run 
# verb = input("Enter the verb: ")
# print(f"I can {verb} better than you.")
# print(5*(f"{verb} "))


#Write a program that:
    #saves a secret number in a variable 
    #asks the user for a number guess.
    #prints a bool True or False depending on the answer
# secret_number = 10
# guess = int(input("Enter your guess number: "))
# print(guess == secret_number)


# x = int(float(input("Enter the value of x: ")))
# y = int(float(input("Enter the value of y: ")))
# if x == y:
#     print(f"{x} is equal to {y}.")
# else:
#     print(f"{x} is not equal to {y}.")


#Write a program that:
    #Saves a secret number
    #asks the user for a number guess
    #print whether the guess is too low, too high, or the same as the secret
# secret = 16
# guess = int(input("Enter your guess for the number: "))
# if guess == secret:
#     print("You guess it right.")
# elif guess >= 2*secret:
#     print("Your guess is too high.")
# elif guess <= secret/2:
#     print("Your guess is too low.")
# else:
#     print("Your guess is somewhat around the secret number.")


# # Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out one of the following strings: 

# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

number = int(input("Enter the value of number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("Your guessed number is zero.")



























