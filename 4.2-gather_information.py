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
tickets_requested = int(tickets_requested)

# Calculate the price (number of tickets multiplied by the price) and assign it to a variable
amount_due = tickets_requested * TICKET_PRICE

# Output the price to the screen
print("The total due is ${}".format(amount_due))

# Prompt user if they want to proceed. Y/N?
complete_purchase = input("Would you like to complete your purchase? y/n: ")

if complete_purchase == "y" or "Y" or "yes" or "YES":
    complete_purchase = True
else:
    complete_purchase = False

print("complete+purchase={}".format(complete_purchase))

# If they want to proceed
if complete_purchase is True:
    # print out to the screen "SOLD!" to confirm purchase
    print("Thanks {}, you've completed your order of {} tickets for ${}. Enjoy the show!".format(username, tickets_requested, amount_due))
    # and then decrement the tickets remaining by the number of tickets purchased
    tickets_remaining -= tickets_requested
# Otherwise...
else:
    # Thank them by name
    print("No problem, {}. Thanks anyways for your interest in the show!".format(username))



