# Debugging assignment module 5
# Hannah Martin
# April 28th, 2022

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # TO DO: run program with user input

    
    score = int(input('Enter grade: '))

    if score >= 90:
        print('Your grade is: A')

    elif score >= 80:
        print('Your grade is: B')

    elif score >= 70:
        print('Your grade is: C')

    elif score >= 60:
        print('Your grade is: D')

    else:
        print('Your grade is: F')

     # TO DO: turn it in WITH DEFINING INT 
main()
