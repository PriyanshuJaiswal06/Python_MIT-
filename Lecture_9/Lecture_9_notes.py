a = (lambda x:x%2 == 0)
(a(4))
def do_twice(n, fn):
    return fn(fn(n))
print(do_twice(3, lambda x: x**2))
print((lambda c: c**2)(5))
b = print("5")
print(b)
print(print("5"))
def is_(n):
    return(n**2)
a = is_(5)
print(a)

is_(5)