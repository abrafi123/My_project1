n = input("Enter a number")
count = 0
for X in n:
    if X.isalpha() and X.lower() not in "aeiou":
        count+=1
print("Number of consonent:",count)