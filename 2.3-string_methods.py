## String Methods
quote = "A person who never made a mistake never tried anything new"

# Return how many characters are within the string variable `quote`. Short for Length.
print(len(quote))

# Return a copy of the string variable `quote` in all uppercase letters.
print(quote.upper())

# Calling the uppercase method above doesn't change the original string variable `quote`.
print(quote)

# Return a copy of the string variable `quote` in all lowercase letters.
print(quote.lower())

# Return a copy of the string variable `quote` in title case format.
print(quote.title())

# Return a string from an integer object
print(str(42))

# You can run the following command in the Python REPL to get more information on specific functions and methods. Running it here will just display the help screen when our program runs so we'll comment it out.
# help(str)

## String formatting
## A reusable template that can be populated with different data.

# Create a string that looks like the following example
print("Thanks for learning JavaScript with us Craig")

# Create a string with some format placeholders
subject_template = "Thanks for learning {} with us {}!"
# Call the string format method and pass in a few strings to use in the placeholders.
print(subject_template.format("Python", "Valentina"))
# Pass in some other strings to the placeholders.
print(subject_template.format("Java", "Shadd"))

# Try another example. Note the integer is automatically converted to a string.
print("You just bought {} {}.".format(3, "fidget cubes"))

## Check if a string is contained in another string. Returns a boolean value of either True or False.
print("ham" in "hamster")
print("popcorn" in "hamster")
