def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"
  
    PriceLakeRegular = [110,90]       # Putting prices for days of the week and weekends for regurlars's of Lakewood
    PriceLakeRewards = [80,80]        # Putting prices for days of the week and weekends for rewards's of Lakewood
    
    PriceBridgRegular = [160,60]      # the same above, but in Bridgewood
    PriceBridgRewards = [110,50]

    PriceRidgRegular = [220,150]      # the same above, but in Ridgewood
    PriceRidgRewards = [100,40]

    days = number.split() # Pick up the information about the number of days ... 

    if ( days[0] == "Regular:"):    #checking if the customer is a regular or a rewards
        TypeClient = "Regular"
    else:
        TypeClient = "Rewards"
    
    account1 = 0      # The account/bill for stay in the Lakewood
    account2 = 0      # The account/bill for stay in the Bridgewood
    account3 = 0      # The account/bill for stay in the Ridgewood

    for day in days:       # Calculating the price for the days 
        if "mon" in day or "tues" in day or "wed" in day or "thur" in day or "fri" in day: 
            if TypeClient == "Regular":
                account1 = account1 + PriceLakeRegular[0]
                account2 = account2 + PriceBridgRegular[0]
                account3 = account3 + PriceRidgRegular[0]
            else:
                account1 = account1 + PriceLakeRewards[0]
                account2 = account2 + PriceBridgRewards[0]
                account3 = account3 + PriceRidgRewards[0]
        
        if "sat" in day or "sun" in day: 
            if TypeClient == "Regular":
                account1 = account1 + PriceLakeRegular[1]
                account2 = account2 + PriceBridgRegular[1]
                account3 = account3 + PriceRidgRegular[1]
            else:
                account1 = account1 + PriceLakeRewards[1]
                account2 = account2 + PriceBridgRewards[1]
                account3 = account3 + PriceRidgRewards[1]
   
    # Looking for the best place to stay
    if (account1 < account2 and account1 < account3):
        cheapest_hotel = "Lakewood"
    
    if (account1 < account2 and account3 <= account1):
        cheapest_hotel = "Ridgewood"
    
    if (account2 < account1 and account2 < account3):
        cheapest_hotel = "Bridgewood"
    
    if (account2 < account1 and account3 <= account2):
        cheapest_hotel = "Ridgewood"
    


    return cheapest_hotel