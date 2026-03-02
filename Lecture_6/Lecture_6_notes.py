'''x = float(input("Enter the number to find the square root of it: "))
epsilon = 0.01
if  x<=1:
    low = x
    high = 1.0
else:
    low = 1.0
    high = x
guess = (low + high)/2
guess_count = 0
while abs(guess**2 -x)>epsilon:
    if guess**2>x:
        high = guess
    else:
        low = guess
    guess = (low + high)/2
    guess_count += 1
print(f"Total number of guesses is: {guess_count}")
print(f"{guess} is the closest to the square root of {x}.")'''



number = float(input("Enter a number: "))
guess = number / 2.0
guess_count = 0
epsilon = 0.01
while abs(guess*guess - number) >= epsilon:
    guess_count += 1
    guess = guess - (((guess**2) - number) / (2 * guess))
print(guess_count)
print(guess)