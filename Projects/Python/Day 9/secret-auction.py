import os

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("\n")


bidding_data = {}
prices = []

loop = True

def find_highest_bidder(bids):
    highest_bid = max(bids.values())
    winners = [name for name, amount in bids.items() if amount == highest_bid]
    return winners, highest_bid

while loop:
    username = input("Enter your name: ").lower()
    if username not in bidding_data:   
        bid_price = int(input("Enter your bid: $ "))
        bidding_data[username] = bid_price
        prices.append(bid_price)
        another_bidder = input("Is there any another bidder?\n").lower()
        if another_bidder == "yes":
            os.system('cls')
            continue
        else:
            loop = False
    else:
        print(f"There exists a user with the username: {username}")

winners, highest_bid = find_highest_bidder(bidding_data)

if len(winners) == 1:
    print(f"{winners[0].capitalize()} won the auction with a bid of ${highest_bid}!")
else:
    winner_names = ', '.join([w.capitalize() for w in winners])
    print(f"It's a tie! {winner_names} all bid ${highest_bid} — the highest amount!")
