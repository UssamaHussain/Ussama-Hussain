# List of coins we have in the shop
list_of_available_coins_in_shop = [20, 10, 5, 2, 1]

#the the_cost_of_the_item is a variable wich gets item's price // 51
the_cost_of_the_item  = int(input("The price of item >> "))
#the the_amount_paid_by_the_customer is a variable wich gets the price paid by user // 74
the_amount_paid_by_the_customer = int(input("The price paid by customer >> "))

# change is the price we have to give back // (74 - 51 = 23)
change = the_amount_paid_by_the_customer - the_cost_of_the_item

# list of change to save the result
change_list = []

# Iterate through each coin
for coin in list_of_available_coins_in_shop:
    # Calculate the number of coins
    num_coins = change // coin

    # Update the change amount for the next iteration
    change = change % coin

    # Append the change_list if the count is greater than 0
    if num_coins > 0:
        change_list.append(coin)

# Print the result
print("Output:")
for coin in change_list:
    print(coin, end=" ")
