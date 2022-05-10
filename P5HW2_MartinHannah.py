# Math Quiz using loops and functions
    # 05/09/2022
    # CTI-110 P5HW2 - Math Quiz
    # Hannah Martin
    #

import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print(f' {num1}')
print(f'+{num2}')


answer = (num1 + num2)
user_answer = int(input('Enter Answer: '))

if user_answer == answer:
    print("Congrats!! your answer is correct")
elif user_answer < answer:
    print("Sorry, guess is too low")
else: user_answer > answer
print("Sorry your guess is too high")


#print("Number of guesses: ", guesses)

# guesses = (user_answer, - 1)
# create menu options 
