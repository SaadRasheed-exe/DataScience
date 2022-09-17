# Tic Tac Toe
```python
import os
def clear(): return os.system('cls')


grid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lastplayer = 0
play_position = 0
plays = 0
players = ['X', 'O']


def main():

    temp = input('Player 1, choose X or O.').lower()
    if temp == 'o':
        players[0] = 'O'
        players[1] = 'X'
    if temp != 'o' and temp != 'x':
        print('Incorrect choice.')

    while not checkWin():
        showGrid()
        play(0)
        showGrid()
        if plays >= 9:
            if not checkWin():
                print('Its a draw!')
                break
        else:
            if not checkWin():
                play(1)
                showGrid()
    displayWin()


def intro():

    print('TIC TAC TOE')
    print(f'Player 1 is {players[0]} and player 2 is {players[1]}.')
    print('Choose a valid position from the grid to play.')


def showGrid():
    clear()
    intro()
    print('{} {} {}'.format(grid[0], grid[1], grid[2]))
    print('{} {} {}'.format(grid[3], grid[4], grid[5]))
    print('{} {} {}'.format(grid[6], grid[7], grid[8]))


def play(player):
    global plays
    global lastplayer
    print(f'Player {player + 1}!')
    play_position = int(input('Enter the position of your play: '))
    while not checkValid(play_position):
        showGrid()
        play_position = int(input('Enter a valid position of your play: '))
    if checkValid(play_position):
        grid[play_position-1] = players[player]
        showGrid()
        print(f'Player {player + 1} chose position {play_position}')
        input('Press Enter to continue.')
        lastplayer = player + 1
        plays += 1


def checkValid(x):
    while x > 9 or x < 1 or grid[x-1] == 'X' or grid[x-1] == 'O':
        return False
    else:
        return True


def checkWin():
    if grid[0] == grid[1] == grid[2]:
        return True
    elif grid[3] == grid[4] == grid[5]:
        return True
    elif grid[6] == grid[7] == grid[8]:
        return True
    elif grid[0] == grid[3] == grid[6]:
        return True
    elif grid[1] == grid[4] == grid[7]:
        return True
    elif grid[2] == grid[5] == grid[8]:
        return True
    elif grid[0] == grid[4] == grid[8]:
        return True
    elif grid[2] == grid[4] == grid[6]:
        return True


def displayWin():
    global lastplayer
    print(f'Player {lastplayer} wins!')
    print('Press Enter to exit. ')


if __name__ == '__main__':
    main()
```
