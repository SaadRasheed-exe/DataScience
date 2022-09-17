# Snake Game
```python
import curses
from random import randint

# constants
WIN_HEIGHT = 60
WIN_WIDTH = 20
ESC = 27

# arrow keys were mapped to these numbers on my system
UP = 450
DOWN = 456
LEFT = 452
RIGHT = 454

# if the game does not work properly on your system, comment out the section above and uncomment the section below
# UP = curses.KEY_UP
# DOWN = curses.KEY_DOWN
# RIGHT = curses.KEY_RIGHT
# LEFT = curses.KEY_LEFT

snakeSymbol = 'x'
foodSymbol = '@'

# curses setup
curses.initscr()
win = curses.newwin(WIN_WIDTH, WIN_HEIGHT, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

# initializing the variables
key = RIGHT
score = 0
snake = [(4, 11), (4, 10), (4, 9)]
food = (10, 20)

# initial food
win.addch(food[0], food[1], foodSymbol)

while key != ESC:
    # snake speed
    win.timeout(250 - (len(snake) // 5) + len(snake)//10 % 120)

    # read key
    event = win.getch()
    prevKey = key
    key = event if event != -1 else prevKey

    if key not in [RIGHT, LEFT, UP, DOWN, ESC]:
        key = prevKey

    # determine direction
    y, x = snake[0]
    if key == RIGHT:
        x += 1
    elif key == LEFT:
        x -= 1
    elif key == UP:
        y -= 1
    elif key == DOWN:
        y += 1

    # check if snake hits a wall or runs into itself
    if y == 0 or y == WIN_WIDTH - 1 or x == 0 or x == WIN_HEIGHT - 1:
        print('You hit the borders!')
        break
    if (y, x) in snake:
        print('You ate yourself!')
        break

    snake.insert(0, (y, x))

    if (y, x) != food:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    else:
        score += 1
        win.addch(food[0], food[1], ' ')
        while food in snake:
            food = (randint(2, WIN_WIDTH - 2), randint(2, WIN_HEIGHT - 2))
        win.addch(food[0], food[1], foodSymbol)

    # draw snake
    for x, y in snake:
        win.addch(x, y, snakeSymbol)

print(f'Total Score: {score}')

curses.endwin()

```
