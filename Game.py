
from Deck import Deck
from Player import Player
from Dealer import Dealer

class Game:
    def __init__(self, num_decks=1):
        self.deck = Deck(num_decks)
        self.player = Player('Player')
        self.dealer = Dealer()
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
   
    def calculate_hand_value(self, hand):
        hand_value = sum(self.card_values[card.rank] for card in hand)
        num_aces = sum(1 for card in hand if card.rank == 'A')

        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value
    
    def start_round(self):
        self.player.clear_hand()  
        self.dealer.clear_hand()
        self.player.reset_bet()

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
        print(f"Player's Hand Value: {self.calculate_hand_value(self.player.hand)}")

    def player_turn(self):
        # Show the dealer's face-up card
        print("Dealer's face-up card:")
        print(self.dealer.hand[0])  

        # Check if the player's hand can be split
        if len(self.player.hand) == 2 and self.player.hand[0].rank == self.player.hand[1].rank:
            split_option = input("Would you like to split your hand? (y/n): ").lower()
            if split_option == 'y':
                # Split the hand
                if self.player.split_hand(self.deck):  # Provide the deck argument
                    # Player places additional bet for the second hand
                    additional_bet = int(input(f"Place additional bet for split hand (current balance: {self.player.balance}): "))
                    while additional_bet <= 0 or additional_bet > self.player.balance:
                        print("Invalid bet amount. Please enter a valid bet.")
                        additional_bet = int(input(f"Place additional bet for split hand (current balance: {self.player.balance}): "))
                    self.player.place_split_bet(additional_bet)

                    # Deal additional card for each hand
                    self.player.receive_card(self.deck.deal_card(), hand=0)
                    self.player.receive_card(self.deck.deal_card(), hand=1)

                    # Play each hand independently
                    self.play_hand(self.player.hands[0])
                    self.play_hand(self.player.hands[1])
                    return
            else:
                self.play_hand(self.player.hand)
        else:
            pass

        # Loop for the player's turn
        while True:
            action = input("Enter 'hit', 'stand', or 'double' to double down: ").lower()
            if action == 'hit':
                self.player.receive_card(self.deck.deal_card())
                print(self.player.hand[-1])
                print(f"Player's Hand Value: {self.calculate_hand_value(self.player.hand)}")
                if self.calculate_hand_value(self.player.hand) > 21:
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
                print(f"Player's Hand Value: {self.calculate_hand_value(self.player.hand)}")
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
            

