from IPython.display import clear_output
import random
import os
clear_output()


suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
    'eight':8, 'nine':9, 'ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:                      # create a deck of 52 cards
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards += [Card(rank, suit)]
                                      
    def __str__(self):
        return f'This deck has {len(self.all_cards)}'
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)

class Player(): # create a player class that takes a name,amount of money, and hand of cards
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.cards = []
        self.total_value = 0
        self.total_value11 = 0
        
    def hand(self, card):
        if type(card) == list:
            self.cards += card
        else:
            self.cards += [card]
        
    def bet(self, total):
        if total <= self.amount:
            self.amount -= total
            return  True
        else:
            return False

def user_input():
    bet = ''
    amount_range = False
    while bet is not int and not amount_range:
        try:
            bet = int(input('Place your bet.  '))
            amount_range = bet in range(1, player_one.amount + 1)
            clear_output()
        except ValueError:
            clear_output()
    return bet

def invite():
    clear_output()
    response = ''
    responses = ['YES','Yes','yes','NO','No','no']
    while response not in responses:
        clear_output()
        response = input('Would you like to play a game of Blackjack? (type yes or no)   ')
    clear_output()
    if response in ['YES', 'Yes', 'yes']:
        return True
    else:
        return False

######################################################## GAME LOGIC ############################################
while invite():
    os.system('clear')     ########################### this line of code is for mac or unix systems; it's coded different for Windows
    game_deck = Deck()
    game_deck.shuffle()
    game_deck.shuffle()
    name001 = input('please provide a name to continue     ')
    amount001 = ''
    while type(amount001) is not int:
        try:
            amount001 = int(input('how much money do you want to put into your account?      '))
            clear_output()
        except ValueError:
            clear_output()
    player_one = Player(name001, amount001)
    winner = ''
    while not winner:
        dealer = Player('dealer', 0)
        betting = user_input()
        if player_one.bet(betting):
            player_one.hand([game_deck.deal_one(), game_deck.deal_one()])
            player_one.total_value += player_one.cards[-1].value
            player_one.total_value += player_one.cards[-2].value
            dealer.hand([game_deck.deal_one(), game_deck.deal_one()])
            dealer.total_value += dealer.cards[-1].value
            dealer.total_value += dealer.cards[-2].value
        print(f"{player_one.name}'s cards: {player_one.cards[-1]} and {player_one.cards[-2]}")
        print(f"dealer's cards: {dealer.cards[-1]}")
        
        ########################## after receiving cards and placing bet, present player with next set of options ###########
        gambles = ['hit', 'stand', 'double down', 'split', 'surrender']
        gamble = ''
        house = 'House wins!\nBetter luck next time, '+player_one.name+'.'
        while not gamble:
            try:
                clear_output()
                gamble = input("What do you want to do?  (hit, stand, double down, split, surrender) type your choice...    ")
            except ValueError:
                print('type one of the aforementioned options.')
            print(f'{gamble} it is, {player_one.name}.')
            if gamble == 'hit':           ##################################################################################
                clear_output()
                print(player_one.name,' player_one.total_value:  ',player_one.total_value)
                player_one.hand(game_deck.deal_one())
                player_one.total_value += player_one.cards[-1].value  # if you got hit with one card then add that one card only to total value
                count = 1
                print('player_one.total_value: ', player_one.total_value)
                for card in player_one.cards:
                    print('your card '+str(count)+ ' is ' +str(card))
                    if card.value == 11 and player_one.total_value > 21:
                        player_one.total_vallue -= 10
                    count += 1
              
                if player_one.total_value > 21 and player_one.total_value11 > 21:
                    print('You have gone over, '+player_one.name+'.')
                    winner = 'house'
                    print(house)
                    break
                else:
                    gamble = ''
                    continue
            elif gamble == 'stand':       ##################################################################################
                print('dealer.total_value: ', dealer.total_value)
                while dealer.total_value <= player_one.total_value:
                    dealer.hand(game_deck.deal_one())
                    dealer.total_value += dealer.cards[-1].value
                    clear_output()
                    count = 1
                    print('dealer.total_value: ', dealer.total_value)
                    for card in dealer.cards:
                        print('dealer card '+str(count)+' is '+str(card))
                        if card.value == 11 and dealer.total_value > 21:
                            dealer.total_vallue -= 10
                        count += 1
                        if dealer.total_value > player_one.total_value and dealer.total_value <= 21:
                            winner = 'house'
                            print(house)
                            print('dealer.total_value: ', dealer.total_value)
                            break
                if dealer.total_value > 21:
                    winner = player_one.name
                    print(f'Bust\n{player_one.name} wins!')
                    print('dealer.total_value: ', dealer.total_value)
                    break

            elif gamble == 'double down':     #############################################################################
                pass
            elif gamble == 'split':          #############################################################################
                pass
            else:                           ##############################################################################
                clear_output()
                winner = 'House'
                print('House wins!\nBetter luck next time '+player_one.name+'.')
                break
            break
print('See ya!')

