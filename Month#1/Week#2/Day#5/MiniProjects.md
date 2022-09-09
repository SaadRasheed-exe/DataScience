# Quiz Game
```python
from datetime import datetime

questions = [
    'What is the radius of the Earth?',
    'Who was the first President of USA?',
    'How old is Pakistan?',
    'Who won the Asia Cup 2022?',
    'How many months of the year have 28 days?',
    'Exactly how many days are there in a year?',
    'Will 2100 be a leap year?',
    '510 mod 7?',
    'What does Gb stand for in IT terms?',
    'Did you enjoy this game?'
]

answers = [
    ['6371', '6,371', '6563', '6,563', 6371, 6563],
    ['george', 'washington', 'george washington'],
    [str(datetime.now().year - 1947), datetime.now().year - 1947],
    ['pakistan'],
    ['12', 12],
    ['365.25', 365.25],
    ['no'],
    ['6', 6],
    ['gigabit', 'gigabits'],
    ['yes']
]

given_answers = []
score = 0

for i, question in enumerate(questions):
    print(question)
    answer = input('Answer: ').lower()
    given_answers.append(answer)
    score += 1 if answer in answers[i] else 0
    print()

print('Your total score: ', score)

print('Would you like to review your answers?')
choice = input().lower()

if choice == 'y' or choice == 'yes':
    for i, answer in enumerate(given_answers):
        print(questions[i])
        print('Your answer: ', answer)

        print('Correct answer: ', answers[i][0]
              if answer not in answers[i] else answer)
        print()
```

# Number Guessing Game
```python
from datetime import datetime

questions = [
    'What is the radius of the Earth?',
    'Who was the first President of USA?',
    'How old is Pakistan?',
    'Who won the Asia Cup 2022?',
    'How many months of the year have 28 days?',
    'Exactly how many days are there in a year?',
    'Will 2100 be a leap year?',
    '510 mod 7?',
    'What does Gb stand for in IT terms?',
    'Did you enjoy this game?'
]

answers = [
    ['6371', '6,371', '6563', '6,563', 6371, 6563],
    ['george', 'washington', 'george washington'],
    [str(datetime.now().year - 1947), datetime.now().year - 1947],
    ['pakistan'],
    ['12', 12],
    ['365.25', 365.25],
    ['no'],
    ['6', 6],
    ['gigabit', 'gigabits'],
    ['yes']
]

given_answers = []
score = 0

for i, question in enumerate(questions):
    print(question)
    answer = input('Answer: ').lower()
    given_answers.append(answer)
    score += 1 if answer in answers[i] else 0
    print()

print('Your total score: ', score)

print('Would you like to review your answers?')
choice = input().lower()

if choice == 'y' or choice == 'yes':
    for i, answer in enumerate(given_answers):
        print(questions[i])
        print('Your answer: ', answer)

        print('Correct answer: ', answers[i][0]
              if answer not in answers[i] else answer)
        print()
```

# Rock, Paper, Scissor Game
```python
import random

plays = ['R', 'P', 'S']

print('Welcome to Rock Paper Scissors!!!')
print("You can play by entering 'R' for Rock, 'P' for paper or 'S' for scissors.")
print("Enter 'E' to exit.")

beats = {'R': 'S', 'P': 'R', 'S': 'P'}
full_forms = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

user_wins = 0
computer_wins = 0
total_games = 0

user_play = input('Your move: ').upper()
while not user_play == 'E':
    total_games += 1
    while user_play not in plays:
        user_play = input('Please enter a valid move: ').upper()
    computer_play = random.choice(plays)
    print('Computer chose', full_forms[computer_play])
    if beats[user_play] == computer_play:
        user_wins += 1
        print('You win!!!')
    elif beats[computer_play] == user_play:
        computer_wins += 1
        print('Computer wins!!!')
    else:
        print("It's a tie.")
    user_play = input('Your move: ').upper()

print('You won', user_wins, 'out of', total_games, 'games')
print('Computer won', computer_wins, 'out of', total_games, 'games')
```

# Password Manager
```python
import os

filename = 'passwords.txt'


def encrypt(string):
    encrypted = ''
    for char in string:
        encrypted += chr(ord(char) + 3)
    return encrypted


def decrypt(string):
    decrypted = ''
    for char in string:
        decrypted += chr(ord(char) - 3)
    return decrypted


def add_password():
    user_id = input('Enter user ID: ')
    while ' ' in user_id:
        print('There should be no spaces in the user ID.')
        user_id = input('Enter user ID: ')
    password = input('Enter the password: ')
    while ' ' in password:
        print('Passwords cannot have spaces.')
        password = input('Enter the password: ')
    encrypted_password = encrypt(password)
    with open(filename, 'a') as f:
        f.write(user_id + ' ' + encrypted_password + '\n')
        f.close()


def print_passwords():
    with open(filename, 'r') as f:
        lines = f.readlines()
        for entries in lines:
            print('User ID: ', entries.split()[0])
            print('Password: ', decrypt(entries.split()[1]))
            print()
        f.close()
    input('Press enter to continue...')


def get_user_input():
    os.system('CLS')
    print('Choose an option below.')
    print('1. Add new password.')
    print('2. List all the passwords.')
    print('3. Exit.')
    choice = int(input('Enter an option: '))
    print()
    return choice


choice = 0

while choice != 3:
    choice = get_user_input()
    if choice == 1:
        add_password()
    elif choice == 2:
        print_passwords()
    elif choice == 3:
        break
    else:
        print('Enter a valid option.')

```
