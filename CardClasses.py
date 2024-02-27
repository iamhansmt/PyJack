'''
Rank to integer dictionary
Define Ace high (11) value. Ace low (1) value will be taken care of during game play with an if statement.
'''
suits = ('h', 'd', 'c', 's')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
        '9': 9, 'T':10, 'J': 10, 'Q': 10, 'K': 10, 'A':11}

import random

'''
CARD CLASS
Defined to track suit, rank and value
'''
class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + self.suit

'''
DECK CLASS
'''
class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(rank,suit)
                self.all_cards.append(new_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal(self):

        return self.all_cards.pop()

    def __str__(self):

        for card in self:
            print(self.card)

'''
Hand Class
'''

class Hand:

    def __init__(self):
        self.cards = []
        self.values = []
        self.aces = 0

    def calc_values(self):

        "total a hand including adjustments for aces low"
        self.values = [0]

        "check for aces"
        self.aces = 0
        for card in self.cards:
            if card.rank == 'A':
                self.aces += 1

        for card in self.cards:
            self.values[0] += card.value

        for option in range(self.aces):
            self.values.append(self.values[option] - 10)

