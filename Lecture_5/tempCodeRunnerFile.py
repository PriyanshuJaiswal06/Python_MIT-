x = float(input("Enter a number: "))
epsilon = 0.01
num_guess = 0
guess = 0.0
increment = 0.001
while abs(guess**2 - x) >= epsilon and guess**2<=x:
    guess += increment
    num_guess += 1
    print(guess, guess**2, num_guess)
print(f"num guesses = {num_guess}.")
if abs (guess**2 - x) >= epsilon:
    print(f"Failed to find square root of {x}.")
    print(f"Last guess was {guess}.")
    print(f"Last guess square was {guess**2}.")
else:
    print(f"{guess} is the closest to the square root of {x}.")
    print(f"{guess**2} and {x}.")