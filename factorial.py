def factorial():
    store = 1
    n = int(input("Enter a number"))
    if n == 0:
        return 1
    else:
        for X in range(1,n+1):
            store*=X
        return store
print(factorial())