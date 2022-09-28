# 12.	Write a Python program find the factorial of a given number. 
import math
n = int(input("Number: "))

print(math.factorial(n))
# for negative number error
#try: 
 #   print(math.factorial(n))
#except:
 #   print("factorial for negative numbers dont exist")
