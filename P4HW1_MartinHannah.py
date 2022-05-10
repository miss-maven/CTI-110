# CTI-110
# P4HW1 - Score List
# Hannah Martin
# May 5th, 2022
#

# ask user how many scores they want to enter

num_scores = int(input('How many scores do you want to enter? '))
# store in a list
scores = []
# loop for user amount of scores to ask
for i in range(num_scores):
    scores_entered = input("Enter score: ")
    scores.append(scores_entered)
print(scores)

# get math 
import math

# display to user the lowest score then the new list w/o lowest then the average of numbers
min(scores)
print('----------Results----------')
print("Lowest score: ", min(scores))
scores.remove(min(scores))
print("Modified List: ", scores)


# get average of scores on mod list then display

average = sum(scores) / len(scores)
print("Scores Average : ", average)
=
# number of the scores converted to letter grades then display to user

if grade >= 90 and grade <= 100:
    print('Grade A')
elif grade >= 80 and grade <= 89:
    print('Grade B')
elif grade >= 70 and grade <= 79:
    print('Grade C')
elif grade >= 60 and grade <= 69:
    print('Grade D')
elif grade >= 0 and grade <= 59:
    print('Grade F')
else:
    print("Invalid score entered!!! ")

print("---------------------------")
