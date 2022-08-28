# 1.	Write a Python Program for calculating simple interest.

# Simple interest formula is given by: Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate.
Principal = float(input("Enter the principal amount: "))
Time = float(input("Time in Years: "))
ROI = float(input("Rate of Interest (without the %): "))
SI = (Principal*Time*ROI)/100
print(f"Simple Interest is {SI} when {Principal} at {Time} years with {ROI}% interest")
