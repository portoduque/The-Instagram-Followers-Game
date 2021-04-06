import os
import random
from art import logo, vs
from game_data import data

def clear_screen():
    """clean the screen"""
    return os.system('clear')

def format_alternative(account):
    """format and print the data 

    Args:
        account (list): [a list with the account informations]

    Returns:
        [string]: [return the alternative line]
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}."

def is_guess_right(followers_a, followers_b):
    """Ask the guess and check if it is right

    Args:
        followers_a (list): [account A followers number]
        followers_b (list): [account B followers number]

    Returns:
        [bolean]: [return True for right and False for wrong]
    """
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    answer_a = followers_a["follower_count"]
    answer_b = followers_b["follower_count"]

    if answer_a > answer_b:
        return guess == "a"
    else:
        return guess == "b"

score = 0
game_over = False

account_b = random.choice(data)
while not game_over: 
    #The A account turn to be B account
    account_a = account_b
    account_b = random.choice(data)

    #If accounts are the same, changes account B
    while account_a == account_b:
        account_b = random.choice(data)

    #Print A account
    print(logo) 
    print(f"Compare A: {format_alternative(account_a)}")

    #Print B account
    print(vs)
    print(f"Against B: {format_alternative(account_b)}\n")

    if is_guess_right(account_a, account_b):
        score += 1
        clear_screen()
        print(f"You're right! Current score: {score}.\n")
    else:
        game_over = True
        clear_screen()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


