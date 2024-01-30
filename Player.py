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

