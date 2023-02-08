#!/usr/bin/env python3
from random import randint
from time import time

rounds = int(input("Round Count (Rec. <=100): "))
mode = int(input("Mode Select (+=1, -=2, x=3, ÷=4 (floor div.), MIXED=5): "))
correct = 0
incorrect = 0
count = 1

start = time()
for i in range(rounds):
	num1 = randint(1,20)
	num2 = randint(1,20)
	
	if mode == 1:
		print(f"{count}/{rounds}) {num1} + {num2}")
		answer = int(input(">"))
		if (num1+num2) == answer:
			correct += 1
		else:
			incorrect += 1
	
	elif mode == 2:
		print(f"{count}/{rounds}) {num1} - {num2}")
		answer = int(input(">"))
		if (num1-num2) == answer:
			correct += 1
		else:
			incorrect += 1
		
	elif mode == 3:
		print(f"{count}/{rounds}) {num1} × {num2}")
		answer = int(input(">"))
		if (num1*num2) == answer:
			correct += 1
		else:
			incorrect += 1
		
	elif mode == 4:
		print(f"{count}/{rounds}) {num1} ÷ {num2} (floor div.)")
		answer = int(input(">"))
		if (num1//num2) == answer:
			correct += 1
		else:
			incorrect += 1
		
	elif mode == 5:
		operation = randint(1,4)
		
		if operation == 1:
			print(f"{count}/{rounds}) {num1} + {num2}")
			answer = int(input(">"))
			if (num1+num2) == answer:
				correct += 1
			else:
				incorrect += 1
		
		elif operation == 2:
			print(f"{count}/{rounds}) {num1}  - {num2}")
			answer = int(input(">"))
			if (num1-num2) == answer:
				correct += 1
			else:
				incorrect += 1
	
		elif operation == 3:
			print(f"{count}/{rounds}) {num1} × {num2}")
			answer = int(input(">"))
			if (num1+num2) == answer:
				correct += 1
			else:
				incorrect += 1
	
		elif operation == 4:
			print(f"{count}/{rounds}) {num1} ÷ {num2} (floor div.)")
			answer = float(input(">"))
			if (num1//num2) == answer:
				correct += 1
			else:
				incorrect += 1
		
	count += 1
		
end = time()
total = end - start
round(total,0)
total = int(total)

seconds = 0
minutes = 0
hours = 0

for i in range(total):
	seconds += 1
	
	if seconds == 60:
		seconds = 0
		minutes += 1
		
	if minutes == 60:
		minutes == 0
		hours += 1
	
print("##### SCORE #####")
print(f"Out of {rounds} questions:")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Time Taken: {hours}:{minutes}:{seconds}")
