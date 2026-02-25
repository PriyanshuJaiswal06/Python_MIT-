x = float(input("Enter the number to find the square root of it: "))
epsilon = 0.01
low = 0
if  x<1:
    high = 1
else:
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
print(f"{guess} is the closest to the square root of {x}.")