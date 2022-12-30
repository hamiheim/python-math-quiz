#!/usr/bin/env python3
# Import required libraries
from random import randint
from os import name, system
import time
from math import modf

# Define function to clear console for ease of reading.
# Might use this later to clear after each question as well 
# if a report of incorrect answers is listed at the end.
def clear_screen():
    system("cls" if name == "nt" else 'clear')
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
        if rnds == 25 or rnds == 50 or rnds == 100 or rnds == 5: #Added 5 rounds for testing
            print()
            break
        else:
            print("INVALID INPUT! Please enter 25, 50, or 100")
            continue
    except ValueError:
        print("INVALID INPUT! Please enter 25, 50, or 100")
        continue
while True:
    try:
        oper = int(input("What kind of test would you like; 1) Addition, 2) Multiplication, 3) Subtraction, or 4) Division? "))
        if oper == int(1):
            print(f"Your addition quiz will consist of {rnds} questions. Good luck!")
            time.sleep(2)
            # Define start time and start test
            start = time.time()
            for z in range(int(rnds)):
                clear_screen()
                num1 = randint(0,50)
                num2 = randint(0,50)
                prob = str(num1) + "+" + str(num2)
                q.append(prob)
                print(f"{ques}/{rnds}) {num1} + {num2}")
                a.append(num1 + num2)
                ans = num1 + num2
                while True:
                    try:
                        uans =  int(input("> "))
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
            break
        elif oper == int(2): 
            print(f"Your multiplication quiz will consist of {rnds} questions. Good luck!")
            time.sleep(2)
            # Define start time and start test
            start = time.time()
            for z in range(int(rnds)):
                clear_screen()
                num1 = randint(0,12)
                num2 = randint(0,12)
                prob = str(num1) + "*" + str(num2)
                q.append(prob)
                print(f"{ques}/{rnds}) {num1} * {num2}")
                a.append(num1 * num2)
                ans = num1 * num2
                while True:
                    try:
                        uans =  int(input("> "))
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
                    a.remove(num1 * num2)
                    ua.remove(uans)
                else:
                    incor = incor + 1
                    ques = ques + 1
            # Define end time
            end = time.time()
            break
        elif oper == int(3):
            print(f"Your subtraction quiz will consist of {rnds} questions. Good luck!")
            time.sleep(2)
            # Define start time and start test
            start = time.time()
            for z in range(int(rnds)):
                clear_screen()
                num1 = randint(0,50)
                num2 = randint(0,50)
                # Prevent negative differences)
                if int(num1) < int(num2):
                    prob = str(num2) + "-" + str(num1)
                    q.append(prob)
                    print(f"{ques}/{rnds}) {num2} - {num1}")
                    a.append(num2 - num1)
                    ans = num2 - num1
                else:
                    prob = str(num1) + "-" + str(num2)
                    q.append(prob)
                    print(f"{ques}) {num1} - {num2}")
                    a.append(num1 - num2)
                    ans = num1 - num2
                while True:
                    try:
                        uans =  int(input("> "))
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
                    if int(num1) < int(num2):
                        a.remove(num2 - num1)
                    else:
                        a.remove(num1 - num2)
                    ua.remove(uans)
                else:
                    incor = incor + 1
                    ques = ques + 1
            # Define end time
            end = time.time()
            break
        elif oper == int(4):
            print(f"Your division quiz will consist of {rnds} questions. Good luck!")
            time.sleep(2)
            # Define start time and start test
            start = time.time()
            # Define list of indexes to use for elementary division
            nume12 = [144, 132, 120, 108, 96, 84, 72, 60, 48, 36, 24, 12]
            nume11 = [121, 110, 99, 88, 77, 66, 55, 44, 33, 22, 11]
            nume10 = [100, 90, 80, 70, 60, 50, 40, 30, 20 ,10]
            nume9 = [81, 72, 63, 54, 45, 36, 27, 18, 9]
            nume8 = [64, 56, 48, 40, 32, 24, 16, 8]
            nume7 = [49, 42, 35, 28, 21, 14, 7]
            nume6 = [36, 30, 24, 18, 12, 6]
            nume5 = [25, 20, 15, 10, 5]
            nume4 = [16, 12, 8, 4]
            nume3 = [9, 6, 3]
            nume2 = [4, 2]
            denum12 = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            denum11 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            denum10 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            denum9 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            denum8 = [8, 7, 6, 5, 4, 3, 2, 1]
            denum7 = [7, 6, 5, 4, 3, 2, 1]
            denum6 = [6, 5, 4, 3, 2, 1]
            denum5 = [5, 4, 3, 2, 1]
            denum4 = [4, 3, 2, 1]
            denum3 = [3, 2, 1]
            denum2 = [2, 1]
            for z in range(int(rnds)):
                clear_screen()
                quotient = randint(2,12)
                if quotient == 12:
                    indint = randint(0,11)
                    num1 = nume12[indint]
                    num2 = denum12[indint]
                elif quotient == 11:
                    indint = randint(0,10)
                    num1 = nume11[indint]
                    num2 = denum11[indint]
                elif quotient == 10:
                    indint = randint(0,9)
                    num1 = nume10[indint]
                    num2 = denum10[indint]
                elif quotient == 9:
                    indint = randint(0,8)
                    num1 = nume9[indint]
                    num2 = denum9[indint]
                elif quotient == 8:
                    indint = randint(0,7)
                    num1 = nume8[indint]
                    num2 = denum8[indint]
                elif quotient == 7:
                    indint = randint(0,6)
                    num1 = nume7[indint]
                    num2 = denum7[indint]
                elif quotient == 6:
                    indint = randint(0,5)
                    num1 = nume6[indint]
                    num2 = denum6[indint]
                elif quotient == 5:
                    indint = randint(0,4)
                    num1 = nume5[indint]
                    num2 = denum5[indint]
                elif quotient == 4:
                    indint = randint(0,3)
                    num1 = nume4[indint]
                    num2 = denum4[indint]
                elif quotient == 3:
                    indint = randint(0,2)
                    num1 = nume3[indint]
                    num2 = denum3[indint]
                elif quotient == 2:
                    indint = randint(0,1)
                    num1 = nume2[indint]
                    num2 = denum2[indint]
                ans = num1/num2
                prob = str(num1) + "/" + str(num2)
                q.append(prob)
                print(f"{ques}/{rnds}) {num1} / {num2}")
                a.append(int(ans))
                while True:
                    try:
                        uans =  int(input("> "))
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
                    a.remove(num1 / num2)
                    ua.remove(uans)
                else:
                    incor = incor + 1
                    ques = ques + 1
            # Define end time
            end = time.time()
            break
        else:
            print("Please enter an operator type")
            continue
    except ValueError:
        print("Please enter an operator type")
        continue

# Calculate score and time to complete
# Attempt to determine if new score is a new "high" score.
tme = round(end-start)
atme = tme/rnds
perc = round((cor/rnds) * 100)
def calc_bonus(rnds, atme, perc):
    if perc < 80:
        return 0
    if atme < 5:
        b = 10
    elif 5 <= atme < 10:
        b = 5
    elif 10 <= atme < 15:
        b = 2.5
    return (rnds * b)
score = score + calc_bonus(rnds, atme, perc)
# Read old high score and store as variable
ohscore = open(".score.txt", "r")
hscore = ohscore.read()
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
print(f"You answered {cor} correctly!")
print(f"You answered {incor} incorrectly!")
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
if int(score) > int(hscore):
    ohscore = open(".score.txt", "w+")
    ohscore.write(str(score))
    ohscore.close()
    ohscore = open(".score.txt", "r")
    hscore = ohscore.read()
    ohscore.close()
    popup = "## NEW HIGH SCORE! ##"
    print("")
    print("#" * len(popup))
    print(popup)
    print("#" * len(popup))
    print("")
print(f"Your average time per question was {atme} seconds")
print(f"Your total time was {m} minutes {s} seconds")
print(f"Your grade is {perc}%")
print(f"Your score is: {score}")
print(f"Your high score is: {hscore}")
