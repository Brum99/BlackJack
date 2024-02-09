import random
from Card import Card  # Import the Card class from the Card module

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = self.generate_deck()
        self.shuffle()

    def generate_deck(self):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        suites = ['♠', '♣', '♦', '♥']
        # Generate a deck with only one rank of cards (let's say '2') and one suite
        deck = [Card('2', suit) for _ in range(self.num_decks) for suit in suites]
        return deck
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
