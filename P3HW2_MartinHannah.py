# CTI-110
# P3HW2 - Pizze Order Revisited
# Hannah Martin
# April 28th, 2022
#

# ask user for number of students and number of slices per student

Students = int(input('How many students do you need pizza for?: '))
SlicesPP = float(input('Enter number of people per pizza 1.5, 2 or 3: '))

# figure out how to make user only enter 3 specific values one of them decimal 
 
print('----Pizza Order------')
print('Number of students: ', Students)

# if else to determine if user is entering a valid choice with statements to user 
if SlicesPP == 1.5:
    print('People per slice 1.5')
    
elif SlicesPP == 2:
    print('People per slice 2')
    
elif SlicesPP == 3:
    print('People per slice 3')
    
else: 
    print('INVALID ENTRY!!!! Should have entered 1.5, 2, 3')
    print('Run Program again')
  
# import math to use ceil
import math
# determine the sum of the students and slices needed then display number as rounded 
sum = (SlicesPP * Students)
print('Pizzas needed: ', (math.ceil(sum)))

#price of pizzas and sales tax to display total to user
price = (math.ceil(sum)) * 5
# calculate then display sales tax at six percent
sales_tax = (price * .06)
total = price + sales_tax

#display the Price and total with only the 2 decimals as standard USD system
print("Price $", f'{total:.2f}')
print('--------------------')




