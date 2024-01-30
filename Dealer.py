from Player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__('Dealer')

    def show_partial_hand(self):
        print("Dealer's Hand:")
        print("Hole Card")
        print(self.hand[1])