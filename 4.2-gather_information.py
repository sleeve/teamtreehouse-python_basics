# 4.2 - Gather Information

import sys

TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining > 0:
    print("There are {} tickets remaining.".format(tickets_remaining))

    username = input("What is your name? ")

    try:
        tickets_requested = int(input("How many tickets would you like, {}? ".format(username)))
        if tickets_requested > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! That's not a valid value. {} Try again...".format(err))
    else:
        amount_due = tickets_requested * TICKET_PRICE
        print("The total due is ${}".format(amount_due))
        complete_purchase = input("Would you like to complete your purchase? y/n: ")

        if complete_purchase.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("Thanks {}, you've completed your order of {} tickets for ${}. Enjoy the show!".format(username, tickets_requested,   amount_due))
            tickets_remaining -= tickets_requested
        else:
            print("No problem, {}. Thanks anyways for your interest in the show!".format(username))

print("All of the tickets are sold out.")

    



