from Deck import Deck
from Player import Player
from Dealer import Dealer
from Hand import Hand

class Game:
    
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)
        self.player = Player('Player')
        self.dealer = Dealer()
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
   
    def calculate_hand_value(self, hand):
        hand_value = sum(self.card_values[card.rank] for card in hand.cards)
        num_aces = sum(1 for card in hand.cards if card.rank == 'A')

        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value
    
    def start_round(self):
        self.player.clear_hands()  # Ensure hands are cleared before starting the round
        self.dealer.clear_hands()
        self.player.reset_bet()

        initial_bet = int(input(f"Place your bet (current balance: {self.player.balance}): "))
        while initial_bet <= 0 or initial_bet > self.player.balance:
            print("Invalid bet amount. Please enter a valid bet.")
            initial_bet = int(input(f"Place your bet (current balance: {self.player.balance}): "))

        if not self.player.place_bet(initial_bet):
            print("Insufficient balance. Please place a valid bet.")
            self.start_round()
            return

        # Deal initial cards
        player_hand = Hand(initial_bet)  # Create a new hand
        self.player.add_hand(player_hand)  # Add the hand to the player's hands
        self.dealer.receive_card(self.deck.deal_card())
        player_hand.add_card(self.deck.deal_card())  # Add card to the player's hand
        self.dealer.receive_card(self.deck.deal_card())
        player_hand.add_card(self.deck.deal_card())  # Add card to the player's hand
        # Show player's hand
        print("Player's Hand:")
        for card in player_hand.cards:
            print(card)
        print(f"Player's Hand Value: {self.calculate_hand_value(player_hand)}")

    def player_turn(self):
        # Show the dealer's face-up card
        print("Dealer's face-up card:")
        print(self.dealer.hand[0])  

        # Loop through each hand of the player
        for hand in self.player.hands:
            if len(hand.cards) == 2 and hand.cards[0].rank == hand.cards[1].rank:
                split_option = input("Would you like to split your hand? (y/n): ").lower()
                if split_option == 'y':
                    if self.player.split_hand(hand):
                        print("Hand split successful!")
                    else:
                        print("Cannot split the hand.")

            # Loop for the player's turn for each hand
            while True:
                action = input("Enter 'hit', 'stand', or 'double' to double down: ").lower()
                if action == 'hit':
                    hand.add_card(self.deck.deal_card())
                    print(hand.cards[-1])
                    print(f"Player's Hand Value: {self.calculate_hand_value(hand)}")
                    if self.calculate_hand_value(hand) > 21:
                        print("Bust! You lose.")
                        self.player.balance -= hand.bet
                        break
                elif action == 'stand':
                    break
                elif action == 'double':
                    if self.player.double_bet(hand.bet):
                        hand.add_card(self.deck.deal_card())
                        print("Player's Hand after doubling down:")
                        for card in hand.cards:
                            print(card)
                        print(f"Player's Hand Value: {self.calculate_hand_value(hand)}")
                    else:
                        print("Insufficient balance. You cannot double your bet.")
                    break

    def dealer_turn(self):
        print("Dealer's Turn:")
        self.dealer.show_partial_hand()
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        while self.dealer.calculate_hand_value(card_values) < 17:  # Pass card_values here
            self.dealer.receive_card(self.deck.deal_card())
        print("Dealer's Hand:")
        for card in self.dealer.hand:
            print(card)
        print(f"Dealer's Hand Value: {self.dealer.calculate_hand_value(card_values)}")  # Pass card_values here as well


    def determine_winner(self):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        for hand in self.player.hands:
            player_value = self.calculate_hand_value(hand)
            dealer_value = self.dealer.calculate_hand_value(card_values)

            if player_value > 21:
                print("Dealer wins!")
                self.player.balance -= hand.bet
            elif dealer_value > 21:
                print("Player wins!")
                self.player.balance += hand.bet
            elif player_value > dealer_value:
                print("Player wins!")
                self.player.balance += hand.bet
            elif player_value < dealer_value:
                print("Dealer wins!")
                self.player.balance -= hand.bet
            else:
                print("It's a tie! Bet returned to the player.")

    def play(self):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        while True:
            self.start_round()
            self.player_turn()
            if self.player.calculate_hand_value(card_values) <= 21:  # Pass card_values here as well
                self.dealer_turn()
                self.determine_winner()
            print(f"Player's Balance: {self.player.balance}")
            if input("Play again? Game Class (y/n): ").lower() != 'y':
                break

    def play_hand(self, hand):
        while True:
            action = input("Enter 'hit' or 'stand': ").lower()
            if action == 'hit':
                hand.append(self.deck.deal_card())
                print(hand[-1])
                print(f"Hand Value: {self.calculate_hand_value(hand)}")
                if self.calculate_hand_value(hand) > 21:
                    print("Bust! You lose.")
                    return 'lose'
            elif action == 'stand':
                return 'stand'
            