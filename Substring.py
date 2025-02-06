#Check for substring
#using if-else statement:

n = input("Enter a string")
m = input("Enter another string")
if m in n:
    print("substring is found")
else:
    print("Substring is not found")
    
#using split() method:

n = input("Enter a string")
m = input("Enter a substring")
s = n.split()
if m in s:
    print("Found")
else:
    print("Not found")