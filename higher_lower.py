#HIGHER LOWER GAME (BUT WITH INSTAGRAM FOLLOWERS)
from art import logo, vs
from game_data import data
from random import randint

print(logo)

def random_selection():
    """Gets a random number from randint and returns the number as an index and person from 'data' list."""
    index = randint(1, len(data) - 1)
    person = data[index]
    return [index, person]

score = 0
a = random_selection()
b = random_selection()
#To ensure 'a' and 'b' never wind up being the same random selection
while b == a:
    b = random_selection()

print(f"Compare A: {a[1]['name']}, a {a[1]['description']}, from {a[1]['country']}.")

print(vs)

print(f"Compare B: {b[1]['name']}, a {b[1]['description']}, from {b[1]['country']}.")

print("Who has more followers? Type 'A' or 'B': ")

# print(data.pop())
# print(data)