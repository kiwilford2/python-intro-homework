# Ask the user for a number and convert to an integer

num = int(input("Enter a number: "))

# First block: check sign (positive, negative, or zero)

if num > 0:
    print(f"{num} is positive.")

elif num < 0:
    print(f"{num} is negative.")

else:
    print(f"{num} is zero.")

# Second block: check parity (even or odd)

if num % 5 == 0:
    print(f"{num} is even.")

else:
    print(f"{num} is odd.")

#Output: 
# Enter a number: 13
# 13 is positive.
# 13 is odd.