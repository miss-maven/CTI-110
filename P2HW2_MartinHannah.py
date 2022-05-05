# CTI-110
# P2HW2 - Score Avg
# Martin Hannah 
# April 14th, 2022


# ask user to enter seven seperate scores with possible decimals

score1 = float(input("Enter first score: "))
score2 = float(input("Enter second score: "))
score3 = float(input("Enter third score: "))
score4 = float(input("Enter fourth score: "))
score5 = float(input("Enter fifth score: "))
score6 = float(input("Enter sixth score: "))
score7 = float(input("Enter seventh score: "))

# make a list with all scores from user input

scores = [score1, score2, score3, score4, score5, score6, score7]

# locate then remove the lowest value from the list of scores display min and mod list

min(scores)
print("----------Results----------")
print("Lowest Score : ", min(scores))
scores.remove(min(scores))
print("Modified List : ", scores)

# get average of scores on mod list then display

average = sum(scores) / len(scores)
print("Scores Average : ", average)
print("---------------------------")

