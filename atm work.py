balance=10000.00
withdraw=int(input("enter a number:"))
if withdraw>0:
    if withdraw%100==0:
        if withdraw<=balance:
            balance-=withdraw
            print("transction successful")
            print("available balance:",balance)
        else:
             print("insufficient balance")
    else:
         print("enter amount in multiples of 100")
else:
    print("invalid amount")