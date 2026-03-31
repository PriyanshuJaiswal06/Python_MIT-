
#To find the root of a expression between 1 and 2 in 3 deciaml precision
low = 1
high = 2

count = 0
while count < 10:
    guess = round(((low+high)/2.0),3)
    a = (guess)**3 - guess - 4
    if a<0:
        low = guess
    else:
        high = guess
    guess = round(((low+high)/2.0),3)
    #a = (guess)**3 - guess - 4
    count += 1
    
print(guess)



#Function as a parameter
def calc(op, x, y):
    return op(x, y)
def add(a, b):
    return a+b
def sub(a, b):
    #print("Absolute difference is: ")
    return abs(a-b)
def mul(a, n):
    return a*n
def div(a, b):
    if b!=0:
        return a/b
    print("Denominator was 0.")
print(calc(add, 2, 4))
print(calc(sub, 2, 10))
print(calc(mul, calc(sub, 2, 10), 7))
res = calc(div, 2, 0)
 

def func_a():
    print("inside function a")
def func_b(y):
    print("inside function b")
    return y
def func_c(f, z):
    print("inside function c")
    return f(z)
print(func_a())
print(5 + func_b(2))
print(func_c(func_b, 3))


