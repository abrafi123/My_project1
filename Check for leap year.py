
#Check for leap year
#using condition
year = int(input("Enter a year"))
if year % 4 == 0:
    print(year,"is a leap year")
elif year % 100 != 0:
    print(year,"is not a leap year")
elif year % 400 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#using lambda function
year = int(input("Enter a year"))
X = lambda a:(a%4==0 and a%100!=0) or (a%400==0)
if X(year):
    print(year, "is a leap year")
else:
    print(year,"is not a leap year")