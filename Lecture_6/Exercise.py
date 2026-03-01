#Write a code to do the bisection search to find the cube root of postive cubes within some epsion.
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
