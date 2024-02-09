class Hand:
    def __init__(self, bet):
        self.cards = []
        self.bet = bet

    def add_card(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    def calculate_value(self):
        hand_value = 0
        num_aces = 0

        for card in self.cards:
            if card.rank.isdigit():
                hand_value += int(card.rank)
            elif card.rank in ['J', 'Q', 'K']:
                hand_value += 10
            elif card.rank == 'A':
                num_aces += 1
                hand_value += 11  # Initially count A as 11

        # Adjust the value of Aces if needed
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10  # Change the value of Ace from 11 to 1
            num_aces -= 1

        return hand_value
