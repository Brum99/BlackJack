
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.balance = 100
        self.bet = 0



    def place_bet(self, amount):
        if amount <= self.balance:
            self.bet += amount
            return True
        else:
            return False

    def double_bet(self):
        if self.balance >= self.bet:  # Check if balance is enough to double the bet
            self.bet *= 2
            return True
        else:
            return False

    def receive_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def reset_bet(self):
        self.bet = 0

    def calculate_hand_value(self, card_values):
        hand_value = sum(card_values[card.rank] for card in self.hand)
        for card in self.hand:
            if card.rank == 'A' and hand_value > 21:
                hand_value -= 10
        return hand_value
    
    def split_hand(self, deck):
        # Check if the player's hand can be split
        if len(self.hand) == 2 and self.hand[0].rank == self.hand[1].rank:
            # Create two separate hands
            hand1 = [self.hand[0]]
            hand2 = [self.hand[1]]
            # Deal an additional card to each hand
            hand1.append(deck.deal_card())
            hand2.append(deck.deal_card())
            # Update the player's bet
            self.bet *= 2
            return hand1, hand2
        else:
            print("Cannot split the hand.")
