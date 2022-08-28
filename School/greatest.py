#Write a Python program to find greatest of three numbers. 
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x > y and x > z:
    print(x, "is greatest")
    
elif y > x and y > z:
    print(y, "is greatest")
    
else:
    print(z, "is greatest")