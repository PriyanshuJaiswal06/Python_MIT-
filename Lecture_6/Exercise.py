'''#Write a code to do the bisection search to find the cube root of postive cubes within some epsilon.
number: int = int(input("Enter the number: "))
epsilon: float = 0.01
low = 0
high = number
guess: float = (low + high)/2
guess_count : int = 0
while abs(guess**3 - number)> epsilon:
    if guess**3> number:
        high = guess
    else:
        low = guess
    guess = (low + high)/2
    guess_count += 1
print("The total number of guesses are %d."% (guess_count))
print("{} is the closest to the cube root of the {}.".format(guess,number))
'''



#Assume you are given an integer 0 <= N <= 1000. 
# Write a piece of Python code that uses bisection search to guess N. 
# The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. 
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

low = 0
high = 1000
N= 999
guess_count = 0
guess = (low + high)//2

while guess != N:
    guess_count += 1
    if guess> N:
        high = guess - 1
    else:
        low = guess + 1
    guess = (low + high)//2
    
print(guess_count)
print(guess)