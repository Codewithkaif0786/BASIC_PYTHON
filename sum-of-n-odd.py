num = int(input("enter a number : "))

sum = 0
x = 1

while x<=num:
     if x%2==1:
         sum = sum + x

         x = x + 1

         print("sum is : ", sum)
