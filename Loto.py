#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def generator(amount):
    list_numbers = []

    while True:
        if len(list_numbers) == amount:
            break

        winning_num = random.randint(1,50)

        if winning_num not in list_numbers:
            list_numbers.append(winning_num)

    return sorted(list_numbers)

print("Welcome to the Lottery numbers generator.")

start = "yes"

while start.lower() == "yes" or start.lower() == "y":
    ask4amount = raw_input("Please enter how many random numbers would you like to have: ")

    try:
        quantity_num = int(ask4amount)
        print generator(quantity_num)
        start = raw_input("Would you like to generate more numbers? (Yes/No) ")
    except:
        print("You didn't enter a number.")
        start = raw_input("Would you like to try again? (Yes/No) ")

print("Understandable, Have a Nice Day (☞ﾟヮﾟ)☞")