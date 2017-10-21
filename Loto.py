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

ask4amount = raw_input("Please enter how many random numbers would you like to have: ")

quantity_num = int(ask4amount)
print generator(quantity_num)

print("END")