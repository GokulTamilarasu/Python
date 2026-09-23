def highest_bidder(bid_details):
    highest_bid=0
    for key in bid_details:
        bidder=key
        if bid_details[key] > highest_bid:
            highest_bid=bid_details[key]
    print(f'The highest bidder was {bidder} with ${highest_bid}')


print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
bid_details = {}
print("Welcome to the auction")
approval=True
while approval:
    name = input("What is your name ?  ")
    bid = int(input("What is your bid ? "))
    bid_details[name] = bid
    continuation = input("Are there other bidders ? yes or no \n")
    if continuation!='yes':
        approval=False
highest_bidder(bid_details)
