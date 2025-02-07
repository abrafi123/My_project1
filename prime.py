#Check the prime number
number = int(input("Enter a number"))
count = 0
for X in range(2,(number//2+1)):
    if (number % X == 0):
        count+=1
        break
if (count == 0 and number>1):
        print("%d is a prime"%number)
else:
        print("%d is not prime"%number)
        