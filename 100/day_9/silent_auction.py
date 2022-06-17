def find_highest_bidder(Bidders):
    max_bid = None
    max_bidder = None
    for Name, Bid in Bidders.items():
        if max_bid == None or Bid > max_bid :
            max_bid = Bid
            max_bidder = Name

    return Name

def main():
    print("Welcome to the silent auction program.")
    bidders = {}

    finished = False
    while not finished:
        name = input("What is your name? ")
        amount = int(input("What is your bid? Rs."))

        bidders[name] = amount #dictionary storing name and bid values

        again = input("Are there any other bidders? Type 'yes' or 'no' : ").lower().strip()
        if again == 'no':
            break
        elif again == 'yes':
            continue
        
    highest_bidder = find_highest_bidder(bidders)
    print(f"The winner is {highest_bidder} with a bid of Rs.{bidders[highest_bidder]}")


main()