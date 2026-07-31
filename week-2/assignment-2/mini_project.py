# Mini Project - Temperature Converter

# Ask the user for temperature in Fahrenheit and covert input to a float
fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = (fahrenheit -32) * 5 / 9

# Print formatted output using an f-strin rounded to one decimal place (.1f)
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")

# Output
# Enter a temperature in Fahrenheit: 98
# 98.0°F is 36.7°C.