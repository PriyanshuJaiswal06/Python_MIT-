#Write code that satisfies the following spec:
#Return true if d divides n evenly else,false
def divisible(n: int, d: int) -> bool:
    """Check whether the number is divisible by d"""
    return n % d == 0
#print(divisible(10,3))
#print(divisible(195,13)) 



#To find the sum of odd number in a given range
def odd_sum(a: int, b: int) -> int:
    sum = 0
    for i in range(a, b+1):
        if is_odd(i):
            sum += i
    return sum
def is_odd(a):
    return a % 2 != 0
#print(odd_sum(2, 2))


#Write code that check whether a given string is palindrome or not
def is_palindrome(a: str)-> bool:
    """Check whether a given string is palindrome or not"""
    return a == a[::-1]
#print(is_palindrome("222"))
#print(is_palindrome("2222"))
#print(is_palindrome("abc"))





def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    value = a*(x**2) + b*x + c
    return value
#print(eval_quadratic(1, 1, 1, 1)) 

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    value1 = a1*(x1**2) + b1*x1 + c1
    value2 = a2*(x2**2) + b2*x2 + c2
    sum = value1 + value2
    print(sum)
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1))