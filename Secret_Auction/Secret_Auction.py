import os

bids = {}
flag = True

def bidder ():
    name = input("Enter you name.\n")
    bid = input("Enter your bid. \n")
    bids [name] = bid

def highest():
    for key in bids:
        temp = 0
        temp1 = ""
        if temp < int(bids[key]):
            temp = bids[key]
            temp1 = key
    print (f"the highest bid is ${temp} made by {temp1}")

while flag:
    os.system('cls') 
    bidder()
    os.system('cls') 
    check = input ("Are there more users to bid? Y/N . \n")
    check = check.lower()
    if check == "y":
        flag = True
    else:
        flag = False
        highest()

        



