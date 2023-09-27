#!/usr/bin/env python3
# Import required libraries
import random
import os
import time
from math import modf

# Define function to clear console for ease of reading.
# Might use this later to clear after each question as well 
# if a report of incorrect answers is listed at the end.
def clear_screen():
    os.system('clear')
clear_screen()

# Reset counters for questions and correct/incorrect answers
cor = 0
incor = 0
ques = 1
score = 0

# Define list of questions and answers
a = []
q = []
ua = []

# Check for high score file and create if absent
try:
    file = open(".score.txt", "r")
except FileNotFoundError:
    file = open(".score.txt", "w")
    file.write("0")
    file.close()

# Define number (integer) of questions to be asked.
# between 25, 50, or 100; included a hidden option of
# 5 for testing; this can be commented.
while True:
    try:
        rnds = int(input("How many questions; 25, 50, or 100? "))
        if rnds == 25:
            print("Your quiz will consist of 25 questions. Good luck!")
            time.sleep(1.5)
            break
        elif rnds == 50:
            print("Your quiz will consist of 50 questions. Good luck!")
            time.sleep(1.5)
            break
        elif rnds == 100:
            print("Your quiz will consist of 75 questions. Good luck!")
            time.sleep(1.5)
            break
        elif rnds == 5:#This amount used for testing
            print("Your quiz will consist of 5 questions. Good luck!")
            time.sleep(1.5)
            break
        else:
            print("INVALID INPUT! Please enter 25, 50, or 100")
            continue
    except ValueError:
        print("INVALID INPUT! Please enter 25, 50, or 100")
        continue

# Define start time and start test
start = time.time()
for z in range(int(rnds)):
    clear_screen()
    num1 = random.randint(0,50)
    num2 = random.randint(0,50)
    prob = str(num1) + "+" + str(num2)
    q.append(prob)
    print(str(ques) + ") " + str(num1) + "+" + str(num2))
    a.append(num1 + num2)
    ans = num1 + num2
    while True:
        try:
            uans =  int(input())
        except ValueError:
            print("Please enter a number")
            continue
        else:
            ua.append(uans)
            break
    if int(ans) == int(uans):
        cor = cor + 1
        ques = ques + 1
        score = score + 10
        q.remove(prob)
        a.remove(num1 + num2)
        ua.remove(uans)
    else:
        incor = incor + 1
        ques = ques + 1
# Define end time
end = time.time()

# Calculate score and time to complete
# Attempt to determine if new score is
# a new "high" score.
perc = round((cor/rnds) * 100)
tme = round((end - start))
atme = round ((tme/rnds))
if rnds == 25 and atme < 5 and perc >= 80:
    score = score + 250
elif rnds == 25 and 5 <= atme < 10 and perc >= 80:
    score = score + 125
elif rnds == 25 and 10 <= atme < 15 and perc >= 80:
    score = score + 75
if rnds == 50 and atme < 5 and perc >= 80:
    score = score + 500
elif rnds == 50 and 5 <= atme < 10 and perc >= 80:
    score = score + 250
elif rnds == 50 and 10 <= atme < 15 and perc >= 80:
    score = score + 125
if rnds == 100 and atme < 5 and perc >= 80:
    score = score + 1000
elif rnds == 100 and 5 <= atme < 10 and perc >= 80:
    score = score + 500
elif rnds == 100 and 10 <= atme < 15 and perc >= 80:
    score = score + 250
# Read old high score and store as variable
ohscore = open(".score.txt", "r")
hscore = ohscore.read()
ohscore.close()
if int(hscore) <= int(score):
    ohscore = open(".score.txt", "w+")
    ohscore.write(str(score))
    ohscore.close()
    ohscore = open(".score.txt", "r")
    hscore = ohscore.read()
else:
    ohscore.close()

# Format time for easy reading
if tme <= 60:
  m = 0
  s = tme
else:
    se,mi = modf(tme/60)
    m = round(mi)
    s = round(se * 60)
clear_screen()

# Print results
print("You answered " + str(cor) + " correctly!")
print("You answered " + str(incor) + " incorrectly!")
if len(q) > 0: #check if any questions were incorrect
    while True:
        rep = input("\nWould you like to see what questions you got wrong? ").lower()
        if rep == 'y' or rep == 'yes':
            print("Incorrect questions: ")
            print(q)
            print("\nYour answers: ")
            print(ua)
            print("\nCorrect answers: ")
            print(a)
            input("\nPress enter to continue...")
            clear_screen()
            break
        elif rep == "n" or rep == "no":
            clear_screen()
            break
        else:
            print("INVALID INPUT! Please enter yes or no ")
            continue
if int(score) == int(hscore):
    popup = "## NEW HIGH SCORE! ##"
    print("")
    print("#" * len(popup))
    print(popup)
    print("#" * len(popup))
    print("")
print("Your average time per question was " + str(atme) + " seconds")
print("Your total time was " + str(m) + " minutes " + str(s) + " seconds")
print("Your grade is " + str(perc) + "%")
print("Your score is: " + str(score))
print("Your high score is: " + str(hscore))
