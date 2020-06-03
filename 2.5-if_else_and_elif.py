# If, Else and Elif

## equality or comparison operator `==`
fruit = "apples"
print(fruit == "apples") # True
print(fruit == "oranges") # False

## import hello.py example
first_name = input("What is your fist name?  ")
print("Hello,", first_name)
if first_name == "Steve":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the Community! Me too!")
else:
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))