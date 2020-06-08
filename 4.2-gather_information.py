# 4.2 - Gather Information

TICKET_PRICE = 10

tickets_remaining = 100

# run this code continuously until we run out of tickets
while tickets_remaining > 0:
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

    # Probably need some logic in here to limit the requested number to tickets that are currently available. So a user can't buy more tickets than we actually have.

    # Calculate the price (number of tickets multiplied by the price) and assign it to a variable
    amount_due = tickets_requested * TICKET_PRICE

    # Output the price to the screen
    print("The total due is ${}".format(amount_due))

    # Prompt user if they want to proceed. Y/N?
    complete_purchase = input("Would you like to complete your purchase? y/n: ")

    if complete_purchase.lower() == "y" or "yes":
        # TODO: Gather credit card information and process it.
        print("Thanks {}, you've completed your order of {} tickets for ${}. Enjoy the show!".format(username, tickets_requested, amount_due))
        tickets_remaining -= tickets_requested
    else:
        print("No problem, {}. Thanks anyways for your interest in the show!".format(username))

# Notify the user that the tickets are sold out
print("All of the tickets are now sold out.".format(username))

    



