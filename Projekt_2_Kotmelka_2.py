"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tereza Kotmelova
email: trydlova@gmail.com
discord: Kotmelka
"""

# Variables
separator = "-----------------------------------------------"
number_of_digits = 4


print("Hi there!")
print(separator)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(separator)

import random


def generate_secret_number():
    first_digit = random.choice(range(1, 10))  #first number is not zero
    other_digits = random.sample(list(set(range(10)) - {first_digit}), 3)  #other numbers
    numbers = [first_digit] + other_digits
    return "".join(map(str, numbers))



def count_bulls_cows(secret, tip):
    bulls, cows = 0, 0
    for item in range(len(secret)):
        if secret[item] == tip[item]:
            bulls += 1
        elif secret[item] in tip:
            cows += 1
    return bulls, cows


def verify_tips(tip):
    if not tip.isdigit() or len(tip) != number_of_digits or len(set(tip)) != number_of_digits:
        return False
    if tip[0] == '0':
        return False
    return True


def print_bulls_cows(bulls, cows):
    bulls_str = "bull" if bulls == 1 else "bulls"
    cows_str = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bulls_str}, {cows} {cows_str}")



def counter_attempts(secret):
    attempts = 0
    max_attempts = 10

    
    while attempts < max_attempts:
        tip = input("Enter a number: ")
        print(separator)

        if not verify_tips(tip):
            print("Invalid tip! Enter four-digit number, without duplicity, not started with zero, and contains numbers only please.")
            continue

        bulls, cows = count_bulls_cows(secret, tip)
        attempts += 1

        if bulls == number_of_digits:
            print(f"Correct, you've guessed the right number {secret}!")
            break
        else:
            print_bulls_cows(bulls, cows)

    if attempts == max_attempts:
        print(f"Game over! Secret number was {secret}.")

if __name__ == "__main__":
    secret_number = generate_secret_number()
    counter_attempts(secret_number)