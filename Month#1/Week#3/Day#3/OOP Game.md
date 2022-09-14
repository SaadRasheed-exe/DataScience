# Card Game
```python
import random
import numpy as np


class Card:
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = ['Ace', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        if suit in Card.suits:
            self.suit = suit
        else:
            raise Exception(f'No suit with name {suit}.')
        if rank in Card.ranks:
            self.rank = rank
        else:
            raise Exception(f'No {rank} rank exists.')

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    # greater than
    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit:
            return Card.ranks.index(self.rank) > Card.ranks.index(other.rank)
        else:
            return False

    # lesser than
    def __lt__(self, other):
        return not self > other


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def popCard(self):
        return self.cards.pop()


class Hand(Deck):
    def __init__(self, label):
        self.cards = []
        self.label = label
        self.wins = 0

    def __str__(self):
        return f'{self.label}: {[str(card) for card in self.cards]}'

    def getLabel(self):
        return self.label

    def getWins(self):
        return self.wins

    def roundWon(self):
        print(f'{self.label} won the round!')
        self.wins += 1


def main():
    deck = Deck()
    players = [Hand('Player 1'), Hand('Player 2'),
               Hand('Player 3'), Hand('Player 4')]

    # distributing the cards to players
    while len(deck) > 0:
        for player in players:
            player.addCard(deck.popCard())

    for round in range(13):
        print('Round', str(round) + ':')
        plays = []
        for player in players:
            plays.append(player.popCard())
        roundWinner = np.argmax(plays)
        players[roundWinner].roundWon()
        print()

    winner = np.argmax([player.getWins() for player in players])
    print(f'{players[winner].label} won the game!!!')


if __name__ == '__main__':
    main()

```
