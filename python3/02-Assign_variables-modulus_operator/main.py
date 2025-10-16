# Get input from user
ounces = int(input())

# There are 32000 oz in 1 US Ton
tons = ounces // 32000
remaining_oz = ounces % 32000
value_1 = round(tons)

# Calculate pounds remaining
pounds = remaining_oz // 16
value_2 = round(pounds)

# Calculate ounces remaining
remaining_oz = remaining_oz % 16
value_3 = round(remaining_oz)

print('Tons:', value_1)
print('Pounds:', value_2)
print('Ounces:', value_3)
