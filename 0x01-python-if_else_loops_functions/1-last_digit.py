#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit_number = number % -10
else:
    last_digit_number = number % 10
if last_digit_number > 5:
    print(f"Last digit of {number} is {last_digit_number} "
          "and is greater than 5 and not 0")
elif last_digit_number == 0:
    print(f"Last digit of {number} is {last_digit_number} and is 0")
else:
    print(F"Last digit of {number} is {last_digit_number} "
          "and is less than 6")
