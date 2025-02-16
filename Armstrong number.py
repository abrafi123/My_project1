#Check for Armstrong number
#An armstrong number is a number that equals the sum of its digit
#370 = 3**3+7**3+0**



num = int(input("Enter a number"))
sum = 0
temp = num
while temp > 0:
    sum = sum + ((temp%10)**3)
    temp = temp // 10
if sum == num:
        print("Armstrong number",sum)
else:
        print("Not a Armstrong number",sum)