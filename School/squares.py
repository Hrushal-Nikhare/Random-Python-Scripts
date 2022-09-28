# 9.	Python Program for Sum of squares of first n natural numbers. 
n = int(input("Number: "))

sum1 = 0
for i in range(0,n+1):
    sum1 += i**2
print(sum1)
