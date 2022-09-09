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
