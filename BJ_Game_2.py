import CardClasses
import itertools
'''
PLAYER CLASS
hand, bankroll, bet
'''

class Player:

    def __init__(self, name, bankroll):
        "Pass in name and starting bankroll"
        self.name = name

        self.hand = []

        self.bankroll = bankroll

    def __str__(self):
        return f'{self.name} has ${self.bankroll}.'

    def printhand(self):

        for x in len(self.hand):
            print(self.hand[x],end=' ')

class Dealer:

    def __init__(self):
        self.deck = []
        self.hand = []

def total(hand):
    "total a hand including adjustments for aces low"
    totals = [0]

    "check for aces"
    aces = 0
    for card in hand:
        if card.rank == 'A':
            aces += 1

    for card in hand:
        totals[0] += card.value

    for option in range(aces):
        totals.append(totals[option] - 10)

    return totals


# Game Setup

player_name = input('What is your name? ')
player1 = Player(player_name,100)
dealer = Dealer()
dealer.deck = CardClasses.Deck()
dealer.deck.shuffle()

play_again = True

while play_again:
    playing = True
    #Deal
    for x in range(2):
        player1.hand.append(dealer.deck.deal())
        dealer.hand.append(dealer.deck.deal())

    "Loop until bet is acceptable"
    bet_not_acceptable = True
    while bet_not_acceptable:
        print(player1)

        try:
            bet = int(input('What is your bet? '))

        except:
            print('That is not a valid bet. Please try again.')

        else:
            if bet > player1.bankroll:
                print('Insufficient bankroll to cover that bet.')
            else:
                bet_not_acceptable = False

    "Loop until player stands."
    player_hit = True
    dealer_hit = True

    "Check for blackjack. If blackjack, player gets 1.5x bet and dealer doesn't play."
    if total(player1.hand)[0] == 21:
        winnings = int(bet*1.5)
        print(f'Blackjack! {player1.name} wins {winnings}')
        print(f'')
        player1.bankroll += winnings
        player_hit = False
        dealer_hit = False
        playing = False

    while player_hit:
        print(f'Dealer shows a {dealer.hand[0]}')
        print(f'{player1.name} has',end=' ')
        for card in player1.hand:
            print(card,end=' ')
        player_totals = total(player1.hand)

        "remove totals over 21"
        for x in reversed(range(len(player_totals))):
            if player_totals[x] > 21:
                player_totals.pop(x)

        "check for bust (no totals left)"
        if len(player_totals) == 0:
            print('\nPlayer busts!!!')
            player1.bankroll -= bet
            playing = False
            dealer_hit = False
            break

        "show player totals"
        print('for',end=' ')
        print(player_totals)

        "Check if player wants to hit"
        response = input('Hit? (y/n) ')
        if response.lower() == 'n':
            player_hit = False
        else:
            player1.hand.append(dealer.deck.deal())

    'Once player stands, dealer plays'
    while dealer_hit:

        print(f'Dealer has', end=' ')
        for card in dealer.hand:
            print(card, end=' ')

        dealer_totals = total(dealer.hand)

        "remove totals over 21"
        for x in reversed(range(len(dealer_totals))):
            if dealer_totals[x] > 21:
                dealer_totals.pop(x)

        "check for bust (no totals left)"
        if len(dealer_totals) == 0:
            print('\nDealer busts!!!')
            print(f'{player1.name} wins {bet}!')
            player1.bankroll += bet
            playing = False
            break

        "show dealer totals"
        print('for',end=' ')
        print(dealer_totals)

        if dealer_totals[0] >= 17:
            dealer_hit = False
        else:
            dealer_hit = True
            dealer.hand.append(dealer.deck.deal())

    if playing:
        if dealer_totals[0] < player_totals[0]:
            print(f'{player1.name} wins {bet}!')
            player1.bankroll += bet
        elif dealer_totals[0] > player_totals[0]:
            print(f'Dealer wins. {player1.name} loses {bet}.')
            player1.bankroll -= bet
        else:
            print(f'Dealer and {player1.name} tie. Push.')

    if player1.bankroll < 1:
        print(player1)
        print(f'{player1.name} is bust.')
        play_again = False
        break

    response = input('Do you want to play again? (y/n) ')
    if response.lower() == 'n':
        play_again = False
        print(f'{player1.name} leaves table with ${player1.bankroll}')
        break

    "if deck is too small, start new deck and shuffle"
    if len(dealer.deck.all_cards) < 26:
        print('Dealer is shuffling.')
        dealer.deck = CardClasses.Deck()
        dealer.deck.shuffle()

    "reset hands"
    player1.hand = []
    dealer.hand = []