#Palindrome check
n = input("Enter a string")
reversed = n[::-1]
if (n == reversed):
    print("Palindrome")
else:
    print("Not palindrome")