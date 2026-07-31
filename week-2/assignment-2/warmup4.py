# Error Message:
#Traceback (most recent call last):
# File "C:\Users\kwilf\OneDrive\Code\python-intro-homework\week-2\assignment-2\warmup4.py", line 4, in <module>
#    next_year = student_age + 1
#                ~~~~~~~~~~~~^~~
#TypeError: can only concatenate str (not "int") to str

# What Caused it:
# input() returns a string, so trying to add the integer 1 to student_age caused a TypeError.

# How I Fixed it:
# Wrapped student_age with int() to covert it from a string to an integer before adding 1.

student_age = input("Enter your age: ")
next_year = int(student_age) + 1
print(f"Next year, I will be {next_year} years old!")
