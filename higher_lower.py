#HIGHER LOWER GAME (BUT WITH INSTAGRAM FOLLOWERS)
from art import logo, vs
from game_data import data
from random import randint

print(logo)

def random_selection():
    """Gets a random number from randint and returns the number as an index and person from 'data' list."""
    index = randint(1, len(data) - 1)
    person = data[index]
    # return [index, person]
    return {
        'index': index,
        'person': person
    }

def compare(a, b):
    if a['person']['follower_count'] > b['person']['follower_count']:
        data.pop(b['index'])
        return 'a'
    else:
        data.pop(a['index'])
        return 'b'

score = 0
a = random_selection()
b = random_selection()
#To ensure 'a' and 'b' never wind up being the same random selection
while b == a:
    b = random_selection()


# print(f"Compare A: {a[1]['name']}, a {a[1]['description']}, from {a[1]['country']}.")
print(f"Compare A: {a['person']['name']}, a {a['person']['description']}, from {a['person']['country']}.")

print(vs)

# print(f"Compare B: {b[1]['name']}, a {b[1]['description']}, from {b[1]['country']}.")
print(f"Compare B: {b['person']['name']}, a {b['person']['description']}, from {b['person']['country']}.")

answer = compare(a,b)
print(f" pssst, the answer is {answer}.")

guess = input("Who has more followers? Type 'A' or 'B': ").lower()
if guess == answer:
    score += 1
    print(f"You're right! Current score: {score}")
else:
    print(f"Sorry, that's wrong. Final score: {score}")
