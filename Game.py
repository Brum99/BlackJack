
from Deck import Deck
from Player import Player
from Dealer import Dealer

class Game:
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)
        self.player = Player('Player')
        self.dealer = Dealer()
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def start_round(self):
            card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
            self.player.clear_hand()
            self.dealer.clear_hand()

            # Reset player's bet to 0
            self.player.bet = 0

            # Place initial bet
            initial_bet = int(input(f"Place your bet (current balance: {self.player.balance}): "))
            while initial_bet <= 0 or initial_bet > self.player.balance:
                print("Invalid bet amount. Please enter a valid bet.")
                initial_bet = int(input(f"Place your bet (current balance: {self.player.balance}): "))

            self.player.place_bet(initial_bet)

            # Deal initial cards
            self.player.receive_card(self.deck.deal_card())
            self.dealer.receive_card(self.deck.deal_card())
            self.player.receive_card(self.deck.deal_card())
            self.dealer.receive_card(self.deck.deal_card())

            # Show player's hand
            print("Player's Hand:")
            for card in self.player.hand:
                print(card)
            print(f"Player's Hand Value: {self.player.calculate_hand_value(card_values)}")



    def player_turn(self):
        # Show the dealer's face-up card
        print("Dealer's face-up card:")
        print(self.dealer.hand[1])

        # Loop for the player's turn
        while True:
            action = input("Enter 'hit', 'stand', or 'double' to double down: ").lower()
            if action == 'hit':
                self.player.receive_card(self.deck.deal_card())
                print(self.player.hand[-1])
                print(f"Player's Hand Value: {self.player.calculate_hand_value(self.card_values)}")
                if self.player.calculate_hand_value(self.card_values) > 21:
                    print("Bust! You lose.")
                    self.player.balance -= self.player.bet
                    break
            elif action == 'stand':
                break
            elif action == 'double':
                additional_bet = self.player.bet
                while additional_bet > self.player.balance:
                    print("Insufficient balance. You cannot double your bet.")
                    additional_bet = int(input("Enter additional amount for doubling your bet: "))
                self.player.place_bet(additional_bet)
                self.player.receive_card(self.deck.deal_card())
                print("Player's Hand after doubling down:")
                for card in self.player.hand:
                    print(card)
                print(f"Player's Hand Value: {self.player.calculate_hand_value(self.card_values)}")
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
        player_value = self.player.calculate_hand_value(card_values)
        dealer_value = self.dealer.calculate_hand_value(card_values)

        if player_value > 21:
            print("Dealer wins!")
            self.player.balance -= self.player.bet
        elif dealer_value > 21:
            print("Player wins!")
            self.player.balance += self.player.bet
        elif player_value > dealer_value:
            print("Player wins!")
            self.player.balance += self.player.bet
        elif player_value < dealer_value:
            print("Dealer wins!")
            self.player.balance -= self.player.bet
        else:
            print("It's a tie! Bet returned to the player.")


    def play(self):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        while True:
            self.start_round()
            print("Player's Hand:")
            for card in self.player.hand:
                print(card)
            print(f"Player's Hand Value: {self.player.calculate_hand_value(card_values)}")  # Pass card_values here
            self.player_turn()
            if self.player.calculate_hand_value(card_values) <= 21:  # Pass card_values here as well
                self.dealer_turn()
                self.determine_winner()
            print(f"Player's Balance: {self.player.balance}")
            if input("Play again? (y/n): ").lower() != 'y':
                break