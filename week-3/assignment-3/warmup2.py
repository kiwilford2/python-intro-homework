# Ask the user for age and convert to integer
age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("Category: Child")

elif age >= 13 and age <= 17:
    print("Category: Teenager")

elif age >= 18 and age <= 64:
    print("Category: Adult")

else:
    print("Category: Senior")

# Output: Enter your age: 36 
# Category: Adult