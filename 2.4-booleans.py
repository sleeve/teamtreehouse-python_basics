# Boolean values

# Create a boolean variable that holds the result of string in string comparison
has_taco = "taco" in "catacombs"
print(has_taco)

print(bool(1)) # = True
print(bool(0)) # = False

# Any non-zero number will be True.
print(bool(42))
# Any object that is not empty will be True
print(bool("burrito"))
# An empty string will be False
print(bool(""))

# The `not` keyword returns the inverse value
print(not True) # = False
print(not False) # = True

# You're able to chain together boolean values in a boolean logic/arithmetic statement
## AND statement where all have to be True for a result of True
print(True and True) # = True
print(True and True and True) # = True
print(True and True and True and False) # = False

## OR statement where one or more have to be True for a result of True
print(False or True) # = True
print(False or False) # = False

print((False or False or True) and (True and False)) # = False
print((False or False or True) and not (True and False)) # = True

# Example Exercise
is_smoker = True
has_kids = True
print(has_kids and not is_smoker) # = False
