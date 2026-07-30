# Event Ticket Admission
# Active Military/Veteran ticket admission for 10% off discount ($36.00).
# Senior Adult 65 or older ticket admission for 5% off discount ($38.00).
# Regular ticket admission pay regular price $40.

base_price = 40.0

is_military = input("Are you active military or a veteran? (yes/no): ").lower()
age = int(input("How old are you? "))

if is_military == "yes":
    price = base_price * 0.90
    print(f"Military Discount Applied! Your ticket price is ${price:.2f}.")
elif age >= 65:
    price = base_price * 0.95
    print(f"Senior Discount Applied! Your ticket price is ${price:.2f}.")
else: 
    price = base_price
    print(f"General Admission: Your ticket price is ${price:.2f}.")