# 9.	Python Program for Sum of squares of first n natural numbers. 
n = int(input("Number: "))

sum1 = sum(i**2 for i in range(1, n+1))
print(sum1)