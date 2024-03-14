import os
from logo import logo


os.system('cls')

user_bid = {}
win_bid = []

while True:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    user_bid[name] = bid
    loop_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if loop_bidder == 'no':
        win_bid = max(user_bid.values())
        for key, value in user_bid.items():
            if win_bid == value:
                print(f"The winner is {key} with a bid of ${value}")
                break
        break
