def add(x, y):
    print(".")
    return x+y
    
def multiply(x, y):
    print(x*y)

add(5,6)
print(add(1,2))
b = add(2, 5)
print(b)
print(multiply(3,4))
a = multiply(8,9)
print(a)

def is_triangular(n):
    """ n is an int > 0
    Returns True if n is triangular, i.e. equals a continued
    summation of natural numbers (1+2+3+...+k), False otherwise """
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return True
    return False
    
print(is_triangular(4))


def count_nums_with_sqrt_close_to (n, epsilon):
    """ n is an int > 2 epsilon is a positive number < 1
        Returns how many integers have a square root within epsilon of n """
    lower = n - epsilon
    higher = n + epsilon
    count = 0
    
    def sqrt(n: int)-> float:
        low = 0
        high = n
        epsilon = 0.01
        guess = (low+high)/2
        while abs(guess**2 - n)> epsilon:
            if guess**2>n:
                high = guess
            else:
                low = guess
            guess = (low+high)/2
        return guess
    #we can use a different approach to find the same answer:
    '''for i in range(n, 2*(n**2)):
            if abs(n - sqrt(i))<epsilon:
                count += 1'''
    for guess in range(n, 2*(n**2)):
        if sqrt(guess)> lower and sqrt(guess)< higher:
            print(guess, sqrt(guess))
            count += 1
            if sqrt(guess) > higher:
                break
    return count
#print(count_nums_with_sqrt_close_to(10, 1))
            
print(type(count_nums_with_sqrt_close_to))
    
a = count_nums_with_sqrt_close_to
print(a(10,1))