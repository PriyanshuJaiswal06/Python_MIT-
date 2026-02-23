#Date - 11/02/2026

#Program to convert  decimal digit number into binary digit number
#we have handled negative number using boolean flag, which is initally set as False,
# and if the input number is negative, then if will become True.
#if the flag value is true, we change the value of num to abs(num)
# After calculating the value of result, we append negative sign -, in the result. 
# num = int(input())
# if num < 0:
#     is_neg = True
#     num = abs(num)
# else:
#     is_neg = False
# binary = ""
# if num == 0:
#   binary = "0"
# while num>0:
#     binary = str(num%2) + binary
#     num = num//2
# print(binary)
# if is_neg:
#     binary = "-" + binary

x = float(input("Enter a number between 0 and 1: "))
p = 0
while ((2**p)*x)%1 != 0:
    print(f"Remainder =   {str((2 ** p)*x - int ((2 ** p)*x))}  {str(p)}")
    p += 1

num = int (x*(2 ** p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str (num%2) + result
    num = num//2

for i in range (p - len (result) ):
    result = '0' + result

result = result [0: -p] + ' .' + result [-p:]

print ('The binary representation of the decimal ' + str(x) + ' is ' + str(result) )
