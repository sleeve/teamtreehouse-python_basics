# 4.2 - Gather Information

TICKET_PRICE = 10

tickets_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable
if tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))
else:
    print("Sorry, no more tickets are available.")

# Gather the user's name and assign it to a new variable
username = input("What is your name? ")

# Prompt the user by name and ask how many tickets they would like
tickets_requested = input("How many tickets would you like, {}? ".format(username))

# Calculate the price (number of tickets multiplied by the price) and assign it to a variable
amount_due = int(tickets_requested) * TICKET_PRICE

# Output the price to the screen
print("The total due is ${}".format(amount_due))





