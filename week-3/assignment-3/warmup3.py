print(not True and False) # not True becomes False; 'False and False' is False

print(True or False and False) # 'and' has higher precedence than 'or': 'False and False' becomes False; 'True or False' is True

print(not (15 > 8)) #Parentheses evaluated first: (15 > 8) is True; 'not True' is False

print(12 == 12 and 6 != 6) #(12 == 12) is True, but (6 != 6) is False; 'True and False' is False

print(not False or not True) #'not' evaluated first: 'not False' is True, 'not True is False; 'True or False is True

#output: 
# False
# True
# False
# False
# True