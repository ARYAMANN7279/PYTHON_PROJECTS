from replit import clear

logo = '''
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
 '''

print(logo)

bidders = {}
max_bid = 0
go_on = 'yes'

while go_on == 'yes':
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    bid = int(input(f"What is your bid {name}? $"))
    bidders[name] = bid
    go_on = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    clear()

for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        winner = key

print(f"The winner is {winner} with a bid of ${max_bid}.")
