#HIGHER LOWER GAME (BUT WITH INSTAGRAM FOLLOWERS)
from art import logo, vs
from game_data import data
from random import randint


def random_selection():
    """Gets a random number from randint and returns the number as an index and person from 'data' list."""
    index = randint(1, len(data) - 1)
    person = data[index]
    return {
        'index': index,
        'person': person
    }

def compare(a, b):
    """Compares the follower account of dict a and dict b and returns the higher dict with updated answer."""
    if a['person']['follower_count'] > b['person']['follower_count']:
        data.pop(b['index'])
        a.update({'answer': 'a'})
        return a
    else:
        data.pop(a['index'])
        b.update({'answer': 'b'})
        return b

def game():
    """Runs the flow of code for higher-lower game. Game continues until user gets the answer wrong."""
    score = 0
    a = random_selection()

    keep_playing = True
    while keep_playing:
        print(logo)
        b = random_selection()
        #To ensure 'a' and 'b' never wind up being the same random selection
        while b == a:
            b = random_selection()

        print(f"Compare A: {a['person']['name']}, a {a['person']['description']}, from {a['person']['country']}.")

        print(vs)

        print(f"Compare B: {b['person']['name']}, a {b['person']['description']}, from {b['person']['country']}.")

        answer = compare(a,b)
        #FOR TESTING
        # print(f" pssst, the answer is {answer['answer']}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == answer['answer']:
            import os
            os.system('clear')
            score += 1
            a = answer
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False

game()