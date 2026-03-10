#Funtion to find the factorial of any given number.
def factorial(n):
    """ Return the factorial of the given number
    """
    fact = 1
    while n>0:
        fact *= n
        n -= 1
    return fact
print(factorial(5))

#Funtion to check whether the number is even or odd.
def is_even(i):
    """Check whether the number is even or odd"""
    return i%2==0

#Function to find if an integer is even or odd.
def is_what(i):
    if i%2==0:
        return "The number is even."
    else:
        return "The number is odd."

print(is_even(9))
print(is_what(-9))

#to find if factor of a number:
def factor(n, i):
    return n%i == 0
num = int(input("Enter a number: "))
i = 1
divisior = []
while i<=num:
    if factor(num,i) == True:
        divisior.append(i)
    i += 1
print(divisior)

#to find all divider of a number and also check whether the number is prime or not:
def is_divisible(n, i):
    return n%i == 0

num = int(input("Enter a number: "))
factors = []
i = 1
flag = True
while i<=num//2:
    if is_divisible(num,i) == True:
        factor.append(i)
    i += 1
factor.append(num)
prime_fact = [1, num]
for i in factors:
    if i not in prime_fact:
        flag = False
        break
if flag == True:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
print(factor)