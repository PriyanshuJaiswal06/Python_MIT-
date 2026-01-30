# Write a program that:
# 1. Asks the user for the verb
# 2.prints "I can _ better than you." where you replace _ with the verb.
# then prints the verb 5 times in a row separated by spaces.
#for example, if the user enters RUN, you prints:
# I can run better than you.
# run run run run run 
verb = input("Enter the verb: ")
print(f"I can {verb} better than you.")
print(5*(f"{verb} "))
