# CTI - 110
# P4HW2 - Pizza Order
# Hannah Martin
# 05/09/2022



# ask user for number of students and number of slices per student

Students = int(input('How many students do you need pizza for?: '))
SlicesPP = float(input('Enter number of people per pizza 1.5, 2 or 3: '))

# figure out how to make user only enter 3 specific values one of them decimal 

# if else to determine if user is entering a valid choice with statements to user 
    
        
if SlicesPP in (1.5, 2, 3):
        print('----Pizza Order------')
        import math
        print("Number of students: ", Students)
        sum = (Students / SlicesPP)
        print('Pizzas needed: ', (math.ceil(sum)))

    #price of pizzas and sales tax to display total to user
        price = (math.ceil(sum)) * 5
    
    # calculate then display sales tax at six percent
        sales_tax = (price * .06)
        total = price + sales_tax
        print(f'Price $ ', f'{total:.2f}')
        print('--------------------')
    
else: 
        print('INVALID ENTRY!!!! Should have entered 1.5, 2, 3')
        print('Run Program again')
        SlicesPP = float(input('Enter number of people per pizza again 1.5, 2 or 3: '))

while True:
    choice =str(input('Would you like to run program again? y for yes '))
    if choice == 'y':
        continue
    else:
        print("Goodbye")
        break



