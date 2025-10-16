# Get the base and height measurements from the user
b1 = int(input("Enter the first base measurement: "))
b2 = int(input("Enter the second base measurement: "))
h = int(input("Enter the height measurement: "))

# Calculate the area of the trapezoid
area = ((b1 + b2) / 2) * h

# Print the result
print(f"Trapezoid area: {area} square meters")
