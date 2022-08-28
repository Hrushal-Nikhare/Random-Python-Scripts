# Write a Python program to convert the distance (in feet) to inches, yards, and miles. 

distance_feet = int(input("Distance in Feet: "))
distance_inches = distance_feet * 12
distance_yards = distance_feet / 3
distance_miles = distance_feet / 5280

print("Inches: ", distance_inches)

print("Yards: ", distance_yards)

print("Miles: ",distance_miles)