
from Hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = [[]]  # List to store player's hands
        self.balance = 100
        self.bet = 0 

    def place_bet(self, amount):
        # Logic for placing bet on a hand
        if amount <= self.balance:
            # Assume only one hand initially
            self.bet = amount
            self.balance -= amount
            return True
        else:
            return False

    def add_hand(self, hand):
        self.hands.append(hand)

    def split_hand(self, hand_index):
        if len(self.hands[hand_index].cards) == 2 and self.balance >= self.hands[hand_index].bet:
            # Create two new hands and deal additional cards
            new_hand1 = Hand(self.hands[hand_index].bet)
            new_hand1.add_card(self.hands[hand_index].cards.pop())
            new_hand2 = Hand(self.hands[hand_index].bet)
            new_hand2.add_card(self.hands[hand_index].cards.pop())

            # Add new hands to player's hands
            self.hands.append(new_hand1)
            self.hands.append(new_hand2)

            return True
        else:
            return False

    def clear_hands(self):
        self.hands = []
    
    def reset_bet(self):
        self.bet = 0 
    
    def receive_card(self,new_card):
        self.hands.append(new_card)