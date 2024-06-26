import secret_auction_ascii
from replit import clear

print(secret_auction_ascii.art)

morePlayers = True
confirmed_bids = {}
big_bid = 0
winner = ""

while morePlayers:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    confirmed_bids[name] = bid
    more = input("Are there more bidders? yes/no\n")
    if more == "no":
        morePlayers = False
    if more == "yes":
        clear()

if not morePlayers:
    for bid in confirmed_bids:
        if confirmed_bids[bid] > big_bid:
            big_bid = confirmed_bids[bid]
            winner = bid
    print(f"Biggest bidder is {winner}, who bid: {big_bid}")
