# Comparisons

## Comparison operators
print("hot dogs" != "sandwiches") # True
print(6 > 3) # True
print(6 < 3) # False
print(42 >= 42) # True
print("sunshine" > "rain") # True (only because it's comparing the alphabetical order of the first letter in the words. "s" comes after "r" in the alphabet. So "s" is greater or higher than "r".)

## import hello.py progress
first_name = input("What is your fist name? ")
print("Hello,", first_name)
if first_name == "Steve":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the Community! Me too!")
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))
