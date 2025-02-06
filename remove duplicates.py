#remove duplicates from list in python
n = [2,4,2,5,6]
blank = []
for X in n:
    if X not in blank:
        blank.append(X)
print(blank)

#remove duplicates from string in python
n = input("Enter a string")
blank = ""
for X in n:
    if X not in blank:
        blank+= X
print(blank)