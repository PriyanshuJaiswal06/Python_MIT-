mysum = 0
for i in range (5, 11, 2):
    mysum += i
    if mysum == 45:
        break
    mysum += 1
print (mysum)