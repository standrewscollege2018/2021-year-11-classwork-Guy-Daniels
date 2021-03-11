# this program will run an auction

# this is asking for the prize and reserve price
prize = input("What is the prize: ")
reserve_asking = True
while reserve_asking == True:
    try:
        reserve = float(input("What is the reserve price: $"))
        reserve_asking = False
    except:
        print("Invalid answer")

print("The auction for the", prize ,"has begun")

bid_asking = True
keep_asking = True
highest_bid = 0
highest_name = 0
while keep_asking == True:
    new_name = input("Name: ")
    while bid_asking == True:
        try:
            new_bid = float(input("Bid:"))
            bid_asking = False
        except:
            print("Invalid answer")
    if new_bid == -1 and highest_bid >= reserve:
        keep_asking = False
    elif new_bid == -1 and highest_bid < reserve:
        print("Highest bid does not meet the reserve")
    elif new_bid > highest_bid:
        highest_bid = new_bid
        highest_name = new_name
    else:
        print("please enter a higher bid")
    print("Highest bid so far is", highest_name , "with", highest_bid)
    bid_asking = True

print("the auction for the", prize ,"finished with a bid of", highest_bid)