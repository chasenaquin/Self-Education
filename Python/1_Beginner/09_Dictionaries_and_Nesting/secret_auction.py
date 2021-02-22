from os import system

print("--++==[ SECRET AUCTION ]==++--")

user = input("Name of bidder? ")
bid_amount = int(input("Amount to bid? $"))

bids_dictionary = {}
def bid (user, bid_amount):
    bids_dictionary[user] = bid_amount

bid(user = user, bid_amount = bid_amount)

for key in bids_dictionary:
    print(f"{key} : {bids_dictionary[key]}")
    print(bids_dictionary)


finished = False
while not finished:
    another_user = input("Is there another bidder? (y/n) ").lower()
    if another_user == "y":
        user = input("Name of bidder? ")
        bid_amount = int(input("Amount to bid? $"))
        bid(user = user, bid_amount = bid_amount)
    else:
        highest_bidder = ""
        highest_bid = ""
        for key in bids_dictionary:
            if key > highest_bidder:
                highest_bidder = key
                highest_bid = bids_dictionary[key]
        finished = True
        print(f"The highest bidder is {key} with a bid of: ${bids_dictionary[key]}")




# #Angelas Code
#
# from replit import clear
# from art import logo
# print(logo)
#
# bids = {}
# bidding_finished = False
#
# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
#
# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
