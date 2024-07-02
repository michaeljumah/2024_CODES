def deposit():
    
    while True:
        amount = input("Enter your deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Your Deposit is Zero...try again")
        print("Enter a valid amount")
        
    return amount

deposit()