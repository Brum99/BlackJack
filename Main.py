import pygame
import sys
from button import Button
from Game import Game  # Uncomment this line to import the Game class
import random

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def play_game():
    play()

def draw_card(screen, card_name, position):
    card_x, card_y = card_positions[card_name]
    card_surface = card_sheet.subsurface(pygame.Rect(card_x, card_y, card_width, card_height))
    screen.blit(card_surface, position)

# Load the card sprite sheet
card_sheet = pygame.image.load("assets/cards.png").convert_alpha()

# Define the dimensions of each card on the sheet
card_width = 69
card_height = 98

# Create a dictionary mapping card names to their positions on the sheet

card_values = {
    "ace_of_spades": 11,
    "2_of_spades": 2,
    "3_of_spades": 3,
    "4_of_spades": 4,
    "5_of_spades": 5,
    "6_of_spades": 6,
    "7_of_spades": 7,
    "8_of_spades": 8,
    "9_of_spades": 9,
    "10_of_spades": 10,
    "J_of_spades": 10,
    "Q_of_spades": 10,
    "K_of_spades": 10,

    "ace_of_clubs": 11,
    "2_of_clubs": 2,
    "3_of_clubs": 3,
    "4_of_clubs": 4,
    "5_of_clubs": 5,
    "6_of_clubs": 6,
    "7_of_clubs": 7,
    "8_of_clubs": 8,
    "9_of_clubs": 9,
    "10_of_clubs": 10,
    "J_of_clubs": 10,
    "Q_of_clubs": 10,
    "K_of_clubs": 10,

    "ace_of_diamonds": 11,
    "2_of_diamonds": 2,
    "3_of_diamonds": 3,
    "4_of_diamonds": 4,
    "5_of_diamonds": 5,
    "6_of_diamonds": 6,
    "7_of_diamonds": 7,
    "8_of_diamonds": 8,
    "9_of_diamonds": 9,
    "10_of_diamonds": 10,
    "J_of_diamonds": 10,
    "Q_of_diamonds": 10,
    "K_of_diamonds": 10,
    # Add more card positions as needed
    "ace_of_hearts": 11,
    "2_of_hearts": 2,
    "3_of_hearts": 3,
    "4_of_hearts": 4,
    "5_of_hearts": 5,
    "6_of_hearts": 6,
    "7_of_hearts": 7,
    "8_of_hearts": 8,
    "9_of_hearts": 9,
    "10_of_hearts": 10,
    "J_of_hearts": 10,
    "Q_of_hearts": 10,
    "K_of_hearts": 10,
}
card_positions = {

    "card_back": (120,263),
    "ace_of_spades": (203, 488),
    "2_of_spades": (286, 488),
    "3_of_spades": (370, 488),
    "4_of_spades": (454, 488),
    "5_of_spades": (538, 488),
    "6_of_spades": (621, 488),
    "7_of_spades": (705, 488),
    "8_of_spades": (789, 488),
    "9_of_spades": (872, 488),
    "10_of_spades": (955, 488),
    "J_of_spades": (1039, 488),
    "Q_of_spades": (1123, 488),
    "K_of_spades": (1206, 488),

    "ace_of_clubs": (203, 375),
    "2_of_clubs": (286, 375),
    "3_of_clubs": (370, 375),
    "4_of_clubs": (454, 375),
    "5_of_clubs": (538, 375),
    "6_of_clubs": (621, 375),
    "7_of_clubs": (705, 375),
    "8_of_clubs": (789, 375),
    "9_of_clubs": (872, 375),
    "10_of_clubs": (955, 375),
    "J_of_clubs": (1039, 375),
    "Q_of_clubs": (1123, 375),
    "K_of_clubs": (1206, 375),

    "ace_of_diamonds": (203, 262),
    "2_of_diamonds": (286, 262),
    "3_of_diamonds": (370, 262),
    "4_of_diamonds": (454, 262),
    "5_of_diamonds": (538, 262),
    "6_of_diamonds": (621, 262),
    "7_of_diamonds": (705, 262),
    "8_of_diamonds": (789, 262),
    "9_of_diamonds": (872, 262),
    "10_of_diamonds": (955, 262),
    "J_of_diamonds": (1039, 262),
    "Q_of_diamonds": (1123, 262),
    "K_of_diamonds": (1206, 262),
    # Add more card positions as needed
    "ace_of_hearts": (203, 150),
    "2_of_hearts": (286, 150),
    "3_of_hearts": (370, 150),
    "4_of_hearts": (454, 150),
    "5_of_hearts": (538, 150),
    "6_of_hearts": (621, 150),
    "7_of_hearts": (705, 150),
    "8_of_hearts": (789, 150),
    "9_of_hearts": (872, 150),
    "10_of_hearts": (955, 150),
    "J_of_hearts": (1039, 150),
    "Q_of_hearts": (1123, 150),
    "K_of_hearts": (1206, 150),
}

player_hand = []
dealer_hand = []
player_balance = 0 
game_over = False
global bet
def deal_initial_cards():
    # Clear the hands
    player_hand.clear()
    dealer_hand.clear()

    # Deal two random cards to the player, excluding "card_back"
    player_cards = random.sample([card for card in card_positions.keys() if card != "card_back"], 2)
    player_hand.extend(player_cards)

    # Deal two random cards to the dealer, excluding "card_back"
    dealer_cards = random.sample([card for card in card_positions.keys() if card != "card_back"], 2)
    dealer_hand.extend(dealer_cards)


def dealer_hit(player_doubled):
    global dealer_hand
    global player_balance
    global bet
    for i, card in enumerate(dealer_hand):
        draw_card(SCREEN, card, (50 + i * 100, 300))

    # Calculate the current value of the dealer's hand
    dealer_value = calculate_hand_value(dealer_hand)
    pygame.display.update()
    pygame.time.delay(500)

    # Continue hitting until the value is 17 or above, or bust
    while dealer_value < 17:
        # Deal another card to the dealer
        new_card = random.choice([card for card in card_positions.keys() if card != "card_back"])
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)

        # Draw the card and update the display
        for i, card in enumerate(dealer_hand):
            draw_card(SCREEN, card, (50 + i * 100, 300))

        pygame.display.update()
        pygame.time.delay(500)  # Delay in milliseconds

    if dealer_value > 21:
        # Display a message indicating dealer bust
        bust_message = get_font(30).render("Dealer Busts!", True, "Red")
        SCREEN.blit(bust_message, (50, 150))
        if player_doubled:
            player_balance += bet*2
        else:
            player_balance += bet
        pygame.display.update()

    return dealer_value



def calculate_hand_value(hand):
    # Initialize the hand value
    hand_value = 0

    # Count the number of aces
    num_aces = sum(1 for card in hand if "ace" in card)

    # Calculate the value of non-ace cards
    for card in hand:
        if "ace" not in card:
            card_value = card_values[card]
            hand_value += card_value

    # Add aces to the hand value, considering them as 1 or 11
    for _ in range(num_aces):
        if hand_value + 11 <= 21:
            hand_value += 11
        else:
            hand_value += 1

    return hand_value

# # Define bet amounts
# BET_AMOUNTS = [5, 10, 25]
# current_bet = 0  # Initialize current bet amount

# # Create bet buttons
# bet_buttons = []
# for i, amount in enumerate(BET_AMOUNTS):
#     bet_button = Button(image=None, pos=(200 + i * 150, 600),  # Adjust positions as needed
#                         text_input=f"${amount}", font=get_font(30),
#                         base_color="Blue", hovering_color="LightBlue")
#     bet_buttons.append(bet_button)

def draw_game_state(player_stood, player_busted, player_doubled):
    global player_balance
    global bet
    # Draw player title
    player_surface = get_font(45).render("Player", True, "White")
    SCREEN.blit(player_surface, (50, 450))

    # Draw Dealer title
    dealer_surface = get_font(45).render("Dealer", True, "White")
    SCREEN.blit(dealer_surface, (50, 200))

    # Draw player cards
    player_card_x = 50
    for card in player_hand:
        draw_card(SCREEN, card, (player_card_x, 550))
        player_card_x += 100

    # Draw dealer's cards
    for i, card in enumerate(dealer_hand):
        if player_stood or player_busted:  # If player stood or busted, reveal all dealer cards
            draw_card(SCREEN, card, (50 + i * 100, 300))
        else:  # Otherwise, only reveal the first card
            if i == 0:
                draw_card(SCREEN, "card_back", (50 + i * 100, 300))
            else:
                draw_card(SCREEN, card, (50 + i * 100, 300))


    # Draw buttons with updated text
                
    # Hit button
    pygame.draw.rect(SCREEN, "DarkGreen", (620, 310, 100, 50))  # Hit button
    hit_text_surface = get_font(30).render("Hit", True, "White")
    SCREEN.blit(hit_text_surface, (620, 310))

    # Stand Button
    pygame.draw.rect(SCREEN, "DarkGreen", (620, 410, 100, 50))  # Stand button
    stand_text_surface = get_font(30).render("Stand", True, "White")
    SCREEN.blit(stand_text_surface, (620, 410))

    # Double down button
    pygame.draw.rect(SCREEN, "DarkGreen", (620, 510, 100, 50))  # Double Down button
    double_down_text_surface = get_font(30).render("Double Down", True, "White")
    SCREEN.blit(double_down_text_surface, (620, 510))
    
    # Split button
    pygame.draw.rect(SCREEN, "DarkGreen", (620, 610, 100, 50))  # Split button
    split_text_surface = get_font(30).render("Split", True, "White")
    SCREEN.blit(split_text_surface, (620, 610))

    # Draw game information
    text_surface = get_font(45).render("Player Balance: $"+str(player_balance), True, "White")
    SCREEN.blit(text_surface, (50, 40))

    # Display current bet amount
    if player_doubled:
        bet_text = get_font(30).render(f"Current Bet: $"+str(bet*2), True, "White")
    else:
        bet_text = get_font(30).render(f"Current Bet: $"+str(bet), True, "White")

    SCREEN.blit(bet_text, (50, 100))


def display_result_message(result_message,result_colour):
    result_text = get_font(30).render(result_message, True, result_colour)
    SCREEN.blit(result_text, (50, 150))
    pygame.display.update()


def play(bet):
    global player_balance, player_hand, dealer_hand  # Make necessary variables global

    # Initialize player balance
    player_balance = 1000

    while True:
        deal_initial_cards()  # Deal initial cards when the game starts
        player_stood = False  # Flag to track if the player has chosen to stand
        player_busted = False  # Flag to track if the player has busted
        dealer_busted = False  # Flag to track if the dealer has busted
        player_doubled = False # Flag to trach if the player has doubled their hand
        player_hit = False # Flag to track if the player has hit
        # Clear the screen
        SCREEN.fill("DarkGreen")

        # Event handling and game logic
        while not player_stood and not player_busted and not player_doubled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle player actions (hit or stand)
                    if not player_stood and not player_busted:
                            mouse_pos = pygame.mouse.get_pos()
                            # Hitting
                            if 620 < mouse_pos[0] < 720 and 310 < mouse_pos[1] < 360:
                                # Deal another card to the player
                                player_cards = random.sample(card_positions.keys(), 1)
                                player_hand.extend(player_cards)
                                player_value = calculate_hand_value(player_hand)
                                # Check if the player has busted
                                if player_value > 21:
                                    player_busted = True
                                # Set the player_hit flag to True
                                player_hit = True
                            # Standing
                            
                            elif 620 < mouse_pos[0] < 720 and 410 < mouse_pos[1] < 460:
                                player_stood = True
                            # Double Down
                            elif 620 < mouse_pos[0] < 720 and 510 < mouse_pos[1] < 560 and not player_hit:
                                player_cards = random.sample(card_positions.keys(), 1)
                                player_hand.extend(player_cards)
                                player_value = calculate_hand_value(player_hand)
                                if player_value > 21:
                                    player_busted = True
                                # Display current bet amount
                                bet_text = get_font(30).render(f"Current Bet: $" + str(bet), True, "DarkGreen")
                                SCREEN.blit(bet_text, (50, 100))
                                player_doubled = True
                            # Splitting
                            elif 620 < mouse_pos[0] < 720 and 610 < mouse_pos[1] < 660:
                                # Implement split functionality here
                                pass  # Place, replace with actual split logic


            # Draw the game state
            draw_game_state(player_stood, player_busted, player_doubled)
            pygame.display.update()

        # Dealer's turn
        if not player_busted:
            dealer_value = dealer_hit(player_doubled)
            if dealer_value > 21:
                dealer_busted = True

            # Compare player and dealer hands if both haven't busted
            if not player_busted and not dealer_busted:
                player_value = calculate_hand_value(player_hand)
                if player_value > dealer_value:
                    result_message = "Player wins!"
                    result_colour = "Blue"
                    if player_doubled:
                        player_balance += bet*2
                    else:
                        player_balance += bet
                elif player_value < dealer_value:
                    result_message = "Dealer wins!"
                    result_colour = "Red"
                    if player_doubled:
                        player_balance -= bet*2
                    else:
                        player_balance -= bet
                else:
                    result_message = "Push!"
                    result_colour = "White"
                # Display the result message
                display_result_message(result_message, result_colour)
        else:
            if player_doubled:
                player_balance -= bet*2
            else:
                player_balance -= bet

            display_result_message("Player busted!", "Red")
        # Delay between rounds
        pygame.time.delay(1500)  # Adjust the delay time as needed

        # Reset the game after the round is played out
        reset_game()
        pygame.display.update()

def reset_game():
    # Reset player and dealer hands
    player_hand.clear()
    dealer_hand.clear()

    # Reset relevant flags
    player_stood = False
    player_busted = False

    # Update the display
    pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    while True:
        global bet
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Create buttons for different bet amounts
        BET_BUTTON_5 = Button(image=None, pos=(320, 250),
                              text_input="5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BET_BUTTON_10 = Button(image=None, pos=(640, 250),
                               text_input="10", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BET_BUTTON_15 = Button(image=None, pos=(960, 250),
                               text_input="15", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BET_BUTTON_5, BET_BUTTON_10, BET_BUTTON_15]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the player clicked on any of the bet buttons
                if BET_BUTTON_5.checkForInput(MENU_MOUSE_POS):
                    bet = 5
                    play(bet)
                elif BET_BUTTON_10.checkForInput(MENU_MOUSE_POS):
                    bet = 10
                    play(bet)
                elif BET_BUTTON_15.checkForInput(MENU_MOUSE_POS):
                    bet = 15
                    play(bet)

        pygame.display.update()



if __name__ == "__main__":
    main_menu()
