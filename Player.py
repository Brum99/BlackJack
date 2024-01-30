
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.balance = 100
        self.bet = 0
        self.split_bet = 0  # New attribute to store the bet for the split hand

    def place_bet(self, amount):
        if amount <= self.balance:
            self.bet += amount
            return True
        else:
            return False

    def double_bet(self):
        if self.balance >= self.bet:
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

    def reset_split_bet(self):  # New method to reset split bet
        self.split_bet = 0

    def calculate_hand_value(self, card_values):
        hand_value = sum(card_values[card.rank] for card in self.hand)
        for card in self.hand:
            if card.rank == 'A' and hand_value > 21:
                hand_value -= 10
        return hand_value

    def split_hand(self, deck):
        if len(self.hand) == 2 and self.hand[0].rank == self.hand[1].rank:
            hand1 = [self.hand[0]]
            hand2 = [self.hand[1]]
            hand1.append(deck.deal_card())
            hand2.append(deck.deal_card())
            self.split_bet = self.bet  # Set split bet equal to the initial bet
            return hand1, hand2
        else:
            print("Cannot split the hand.")
            return None, None

    def adjust_balance(self, result):
        if result == 'win':
            self.balance += self.bet
        elif result == 'lose':
            self.balance -= self.bet
        # No change in balance for tie

        if self.split_bet > 0:
            if result == 'win':
                self.balance += self.split_bet
            elif result == 'lose':
                self.balance -= self.split_bet
            # No change in balance for tie
            self.reset_split_bet()  # Reset split bet after the round
