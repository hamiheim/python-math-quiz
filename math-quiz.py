#!/usr/bin/env python3
# Import required libraries
from random import randint
from os import name, system
from time import time, sleep
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


# Define addition function
def addition():
    global ques
    clear_screen()
<<<<<<< HEAD
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    prob = str(num1) + "+" + str(num2)
    q.append(prob)
    print(f"<{ques}/{rnds}>")
    print(f"{num1 : >5}")
    print(f"+ {num2 : >3}")
=======
    num1 = randint(0, 50)
    num2 = randint(0, 50)
    prob = str(num1) + "+" + str(num2)
    q.append(prob)
    print(f"{ques}/{rnds}) {num1} + {num2}")
>>>>>>> main
    a.append(num1 + num2)
    ans = num1 + num2
    while True:
        try:
            uans = int(input("> "))
            ua.append(uans)
            break
        except ValueError:
            print("Please enter a number")
            continue
    if int(ans) == int(uans):
        global cor
        cor = cor + 1
        ques = ques + 1
        global score
        score = score + 10
        q.remove(prob)
        a.remove(num1 + num2)
        ua.remove(uans)
    else:
        global incor
        incor = incor + 1
        ques = ques + 1


# Define multiplication function
def multiplication():
    global ques
    clear_screen()
<<<<<<< HEAD
    num1 = randint(0, 999)
    num2 = randint(0, 99)
    prob = str(num1) + "*" + str(num2)
    q.append(prob)
    print(f"<{ques}/{rnds}>") 
    print(f"{num1 : >5}")
    print(f"* {num2 : >3}")
=======
    num1 = randint(0, 12)
    num2 = randint(0, 12)
    prob = str(num1) + "*" + str(num2)
    q.append(prob)
    print(f"{ques}/{rnds}) {num1} * {num2}")
>>>>>>> main
    a.append(num1 * num2)
    ans = num1 * num2
    while True:
        try:
            uans = int(input("> "))
            ua.append(uans)
            break
        except ValueError:
            print("Please enter a number")
            continue
    if int(ans) == int(uans):
        global cor
        cor = cor + 1
        ques = ques + 1
        global score
        score = score + 10
        q.remove(prob)
        a.remove(num1 * num2)
        ua.remove(uans)
    else:
        global incor
        incor = incor + 1
        ques = ques + 1


# Define subtraction function
def subtraction():
    global ques
    clear_screen()
<<<<<<< HEAD
    num1 = randint(0, 999)
    num2 = randint(0, 999)
=======
    num1 = randint(0, 50)
    num2 = randint(0, 50)
>>>>>>> main
    # Prevent negative differences)
    if int(num1) < int(num2):
        prob = str(num2) + "-" + str(num1)
        q.append(prob)
<<<<<<< HEAD
        print(f"<{ques}/{rnds}>")
        print(f"{num2 : >5}")
        print(f"- {num1 : >3}")
=======
        print(f"{ques}/{rnds}) {num2} - {num1}")
>>>>>>> main
        a.append(num2 - num1)
        ans = num2 - num1
    else:
        prob = str(num1) + "-" + str(num2)
        q.append(prob)
<<<<<<< HEAD
        print(f"<{ques}/{rnds}>")
        print(f"{num1 : >5}")
        print(f"- {num2 : >3}")
=======
        print(f"{ques}) {num1} - {num2}")
>>>>>>> main
        a.append(num1 - num2)
        ans = num1 - num2
    while True:
        try:
            uans = int(input("> "))
            ua.append(uans)
            break
        except ValueError:
            print("Please enter a number")
            continue
    if int(ans) == int(uans):
        global cor
        cor = cor + 1
        ques = ques + 1
        global score
        score = score + 10
        q.remove(prob)
        if int(num1) < int(num2):
            a.remove(num2 - num1)
            ua.remove(uans)
        else:
            a.remove(num1 - num2)
            ua.remove(uans)
    else:
        global incor
        incor = incor + 1
        ques = ques + 1


# Define division function
def division():
    global ques
    clear_screen()
    num1 = randint(2, 9999)
    num2 = randint(2, 12)
    if int(num1) < int(num2):
        ans = num2//num1
        ansr = num2%num1
        prob = str(num2) + "/" + str(num1)
        q.append(prob)
        print("Answers should be submitted by quotient <enter> followed by remainder. "
              "If no remainder, simply enter 0.")
        print(f"{ques}/{rnds}) {num2} / {num1}")
        a1 = str(str(ans) + " R:" + str(ansr))
        a.append(a1)
    else:
        ans = num1//num2
        ansr = num1%num2
        prob = str(num1) + "/" + str(num2)
        q.append(prob)
        print("Answers should be submitted by quotient <enter> followed by remainder. "
              "If no remainder, simply enter 0.")
        print(f"{ques}/{rnds}) {num1} / {num2}")
        a1 = str(str(ans) + " R:" + str(ansr))
        a.append(a1)
    while True:
        try:
            uans = int(input("> "))
            uansr = int(input("> R:"))
            ua1 = str(str(uans) + " R:" + str(uansr))
            ua.append(ua1)
            break
        except ValueError:
            print("Please enter a number")
            continue
    if int(ans) == int(uans) and int(ansr) == int(uansr):
        global cor
        cor = cor + 1
        ques = ques + 1
        global score
        score = score + 10
        q.remove(prob)
        a.remove(a1)
        ua.remove(ua1)
    else:
        global incor
        incor = incor + 1
        ques = ques + 1


# Define mix operation functions
def mix0():
    oper = randint(1, 4)
    if oper == int(1):
        addition()
    elif oper == int(2):
        multiplication()
    elif oper == int(3):
        subtraction()
    elif oper == int(4):
        division()


def mix1():
    oper = randint(1, 2)
    if oper == int(1):
        addition()
    elif oper == int(2):
        multiplication()


def mix2():
    oper = randint(1, 2)
    if oper == int(1):
        addition()
    elif oper == int(2):
        subtraction()


def mix3():
    oper = randint(1, 2)
    if oper == int(1):
        addition()
    elif oper == int(2):
        division()


def mix4():
    oper = randint(1, 2)
    if oper == int(1):
        multiplication()
    elif oper == int(2):
        division()


def mix5():
    oper = randint(1, 2)
    if oper == int(1):
        multiplication()
    elif oper == int(2):
        subtraction()


def mix6():
    oper = randint(1, 2)
    if oper == int(1):
        subtraction()
    elif oper == int(2):
        division()


def mix7():
    oper = randint(1, 3)
    if oper == int(1):
        addition()
    elif oper == int(2):
        multiplication()
    elif oper == int(3):
        subtraction()


def mix8():
    oper = randint(1, 3)
    if oper == int(1):
        addition()
    elif oper == int(2):
        multiplication()
    elif oper == int(3):
        division()


def mix9():
    oper = randint(1, 3)
    if oper == int(1):
        addition()
    elif oper == int(2):
        division()
    elif oper == int(3):
        subtraction()


def mix10():
    oper = randint(1, 3)
    if oper == int(1):
        multiplication()
    elif oper == int(2):
        division()
    elif oper == int(3):
        subtraction()


# Define number (integer) of questions to be asked.
# between 25, 50, or 100; included a hidden option of
# 5 for testing; this can be commented.
while True:
    try:
<<<<<<< HEAD
        rnds = int(input("How many questions; 5, 10, 25, 50, or 100? "))
        if rnds == 5 or rnds == 10 or rnds == 25 or rnds == 50 or rnds == 100:
            print()
            break
        else:
            print("INVALID INPUT! Please enter 5, 10, 25, 50, or 100")
            continue
    except ValueError:
        print("INVALID INPUT! Please enter 5, 10, 25, 50, or 100")
        continue
while True:
    try:
        oper = int(input('What kind of test would you like; 1) Addition, '
                        '2) Multiplication, 3) Subtraction, 4) Division,'
                        'or 5) Mixed? '))
        if oper == int(1):
            print(f'Your addition quiz will consist of {rnds} '
                   'questions. Good luck!')
=======
        rnds = int(input("How many questions; 25, 50, or 100? "))
        if rnds == 25 or rnds == 50 or rnds == 100 or rnds == 5:
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
        oper = int(input("""What kind of test would you like; 1) Addition, 2)
        Multiplication, 3) Subtraction, 4) Division,
                   or 5) Mixed? """))
        if oper == int(1):
            print(f"""Your addition quiz will consist of
            {rnds} questions. Good luck!""")
>>>>>>> main
            sleep(2)
            start = time()
            for z in range(int(rnds)):
                addition()
            end = time()
            break
        elif oper == int(2):
<<<<<<< HEAD
            print(f'Your multiplication quiz will consist of {rnds} '
                   'questions. Good luck!')
=======
            print(f"""Your multiplication quiz will consist of
            {rnds} questions. Good luck!""")
>>>>>>> main
            sleep(2)
            start = time()
            for z in range(int(rnds)):
                multiplication()
            end = time()
            break
        elif oper == int(3):
<<<<<<< HEAD
            print(f'Your subtraction quiz will consist of {rnds} '
                   'questions. Good luck!')
=======
            print(f"""Your subtraction quiz will consist of
            {rnds} questions. Good luck!""")
>>>>>>> main
            sleep(2)
            start = time()
            for z in range(int(rnds)):
                subtraction()
            end = time()
            break
        elif oper == int(4):
<<<<<<< HEAD
            print(f'Your division quiz will consist of {rnds} '
                   'questions. Good luck!')
=======
            print(f"""Your division quiz will consist of
            {rnds} questions. Good luck!""")
>>>>>>> main
            sleep(2)
            start = time()
            for z in range(int(rnds)):
                division()
            end = time()
            break
        elif oper == int(5):
            print("What type of mix operation do you want to test on?")
            mix = input("Select range of operators; i.e. 1,2 or 2,3,4 ")
            if mix == ('1,2'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Addition and Multiplication with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Addition and Multiplication with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix1()
                end = time()
                break
            elif mix == ('1,3'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                f'{rnds} Addition and Subtraction questions. '
                'Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Addition and Subtraction with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix2()
                end = time()
                break
            elif mix == ('1,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Addition and Division with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                      Addition and Division with
                      {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix3()
                end = time()
                break
            elif mix == ('2,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Multiplication and Divsion with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                      Multiplication and Divsion with
                      {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix4()
                end = time()
                break
            elif mix == ('2,3'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Multiplication and Subtraction with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Multiplication and Subtraction with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix5()
                end = time()
                break
            elif mix == ('3,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Subtraction and Division with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Subtraction and Division with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix6()
                end = time()
                break
            elif mix == ('1,2,3'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Addition, Multiplication, and Subtraction with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Addition, Multiplication, and Subtraction with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix7()
                end = time()
                break
            elif mix == ('1,2,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Addition, Multiplication, and Division with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Addition, Multiplication, and Division with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix8()
                end = time()
                break
            elif mix == ('1,3,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Addition, Subtraction, and Divsion with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Addition, Subtraction, and Divsion with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix9()
                end = time()
                break
            elif mix == ('2,3,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of '
                'Multiplication, Subtraction, and Divsion with '
                f'{rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                Multiplication, Subtraction, and Divsion with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix10()
                end = time()
                break
            elif mix == ('1,2,3,4'):
<<<<<<< HEAD
                print(f'Your mix operation quiz will consist of all '
                f'operators with {rnds} questions. Good luck!')
=======
                print(f"""Your mix operation quiz will consist of
                all operators with
                {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix0()
                end = time()
                break
            elif not mix:
<<<<<<< HEAD
                print(f'Unkown Input... Defaulting to all operators!'
                f'Your mix operation quiz will consist of {rnds} questions. Good luck!')
=======
                print(f"""Defaulting to all operators!
                      \nYour mix operation quiz will consist of
                      {rnds} questions. Good luck!""")
>>>>>>> main
                sleep(2)
                start = time()
                for z in range(int(rnds)):
                    mix0()
                end = time()
                break
            else:
                print("Invalid mix operation selected")
                continue
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
    if perc == 100:
        b = 2.5
    elif perc < 80:
        return 0
    if atme < 20:
        b = 10
    elif 20 <= atme < 35:
        b = 7.5
    elif 35 <= atme < 50:
        b = 5
    elif 50 <= atme:
        return 0
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
    se, mi = modf(tme/60)
    m = round(mi)
    s = round(se * 60)
clear_screen()

# Print results
print(f"You answered {cor} correctly!")
print(f"You answered {incor} incorrectly!")
if len(q) > 0:  # check if any questions were incorrect
    while True:
<<<<<<< HEAD
        rep = input("\nWould you like to see what questions you got wrong? ").lower()
=======
        rep = input("""\nWould you like to see
                    what questions you got wrong? """).lower()
>>>>>>> main
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