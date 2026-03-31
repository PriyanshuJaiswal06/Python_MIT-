def h(y):
    x += 1 #leads to an error without line `global x` inside h

x = 5
h(x)
print(x)