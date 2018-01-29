import random


class Players (object):

    def __init__(self,total=100):
        self.total = total
        print(self.total)

    def add_to_total(self,change):
        self.total += change

    def sub_from_total(self,change):
        self.total -= change


class Deck (object):

    cards = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4)

    def __init__(self):
        print('The current deck is full and is comprised of: ')
        print(Deck.cards)

    def deal_card(self):
        card_drawn = random.choice(Deck.cards)
        Deck.cards.append(card_drawn)
        return card_drawn

    def new_deck(self):
        # Create a new deck by resetting the Deck of cards
        Deck.cards = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4)


# Determine if player wants to play
playGame = input('do you want to play? y/n \n')
if playGame == 'y':
    play = True
else:
    play = False
    print('Fine then, be that way.')

# Start game
if play:
    # Establish total for each player.
    p1 = Players()
    dealer = Players()
    playing_deck = Deck()
    # check if both players still have money
    while dealer.total and p1.total > 0:
        # Continue with ze game

        # find out how much the player wants to bet.
        while True:
            try:
                bet_amount = int(input('How much do you want to bet? \n'))
            except:
                print('You didn\'t put in an int...')
                continue
            else:
                print('Your bet amount is: ' + str(bet_amount))
                break
        player_hand = [playing_deck.deal_card()]
        player_hand.append(playing_deck.deal_card())
        dealer_hand = [playing_deck.deal_card()]
        dealer_hand.append(playing_deck.deal_card())
        player_loses = False
        print('The cards in your hand are/is: ')
        print(player_hand)
        if sum(player_hand) > 21:
            print('YOU BUSTED')
            player_loses = True
        elif sum(player_hand) == 21:
            print('You got 21, nice.')
            player_loses = False
        # Determine if you want more cards
        more_cards = input('Do you want to draw another card? y/n \n')
        while more_cards == 'y' and player_loses is False:
            # Another card has been drawn
            player_hand.append(playing_deck.deal_card())
            print('The cards in your hand are/is: ')
            print(player_hand)
            if sum(player_hand) > 21:
                print('BUST')
                player_loses = True
            elif sum(player_hand) == 21:
                print('You got 21, nice.')
                player_loses = False
            more_cards = input('Draw another card? y/n \n')
        if sum(player_hand) > sum(dealer_hand) or sum(player_hand) == 21:
            print('The sum of the dealers cards is: ' + str(sum(dealer_hand)))
            print('The sum of your cards is: ' + str(sum(player_hand)))
            print('You win!!!')
            player_loses = False
        else:
            print('The sum of the dealers cards is: ' + str(sum(dealer_hand)))
            print('The sum of your cards is: ' + str(sum(player_hand)))
            print('You lose!!!')
            player_loses = True
        if player_loses:
            p1.sub_from_total(bet_amount)
            dealer.add_to_total(bet_amount)
            print('Your new total is: ' + str(p1.total))
            print('The dealer has: ' + str(dealer.total))
        else:
            dealer.sub_from_total(bet_amount)
            p1.add_to_total(bet_amount)
            print('Your new total is: ' + str(p1.total))
            print('The dealer has: ' + str(dealer.total))
    else:
        # Check who won.
        if p1.total > dealer.total:
            print('Player wins')
        else:
            print('You lose.')
