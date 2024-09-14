# import clear


# bider = []
# def add_bider(bider_name, bid_amount):
#     new_bider = {}
#     new_bider["name"] = bider_name
#     new_bider["price"] = bid_amount

#     bider.append(new_bider)

#     print(bider)


def find_highest_bider(bider_record):
    highest_bider = 0
    for bid in bider_record:
        bid_amount = bider_record[bid]
        # print(bid_amount)
        
        if bid_amount > highest_bider:
            highest_bider = bid_amount
            bider_name = bid
    print(f"The winner is {bider_name} with ${highest_bider}")   
    






bids = {}
next_bider = True

while next_bider:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: $"))

    bids[name] = bid_price
    
    to_bid = input("Type 'yes' to continue biddig, 'no' to stop: ")
    if to_bid == "no":
        next_bider = False
        find_highest_bider(bids)
    
# print(bids)      
    







