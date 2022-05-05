# Total purchases using variables and expressions
    # April 14th, 2022
    # CTI-110 P2HW1 - Total Purchases
    # Martin Hannah
    

# get 5 different prices from user

price1 = float( input("Enter the price of item one: "))
price2 = float( input("Enter the price of item two: "))
price3 = float( input("Enter the price of item three: "))
price4 = float( input("Enter the price of item four: "))
price5 = float( input("Enter the price of item five: "))

# display results to the user of subtotal after calculating
print("-------Results-------")
subtotal = ((price1) + (price2) + (price3) + (price4) + (price5))
print("Subtotal:", subtotal)

# calculate then display sales tax at seven percent

sales_tax = (subtotal * .07)
print("Sales Tax:", sales_tax)

# calculate the total by adding subtotal and tax and display

total =((sales_tax) + (subtotal))
print("Total: ", total)

        


