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


def dealer_hit():
    global dealer_hand

    # Calculate the current value of the dealer's hand
    dealer_value = calculate_hand_value(dealer_hand)

    # Continue hitting until the value is 17 or above, or bust
    while dealer_value < 17:
        # Deal another card to the dealer
        new_card = random.choice([card for card in card_positions.keys() if card != "card_back"])
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)

        # Draw the card and update the display
        SCREEN.fill("Tan")  # Clear the screen
        for i, card in enumerate(dealer_hand):
            if i == 0:
                draw_card(SCREEN, "card_back", (50 + i * 100, 300))
            else:
                draw_card(SCREEN, card, (50 + i * 100, 300))
        pygame.display.update()

        # Add a delay
        pygame.time.delay(500)  # Delay in milliseconds

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


def play():
    deal_initial_cards()  # Deal initial cards when the game starts
    player_stood = False  # Flag to track if the player has chosen to stand

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not player_stood:  # Only allow actions if player hasn't stood
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if Hit button is clicked
                    if 600 < mouse_pos[0] < 700 and 400 < mouse_pos[1] < 450:
                        # Deal another card to the player
                        player_cards = random.sample(card_positions.keys(), 1)
                        player_hand.extend(player_cards)
                    # Check if Stand button is clicked
                    elif 600 < mouse_pos[0] < 700 and 500 < mouse_pos[1] < 550:
                        player_stood = True

        # Clear the screen
        SCREEN.fill("Tan")

        # Draw player
        player_surface = get_font(45).render("Player", True, "Black")
        SCREEN.blit(player_surface, (50, 450))
        # Draw Dealer
        dealer_surface = get_font(45).render("Dealer", True, "Black")
        SCREEN.blit(dealer_surface, (50, 200))

        # Draw player cards
        player_card_x = 50
        for card in player_hand:
            draw_card(SCREEN, card, (player_card_x, 550))
            player_card_x += 100

        # Draw dealer's cards
        for i, card in enumerate(dealer_hand):
            if i == 0:
                draw_card(SCREEN, "card_back", (50 + i * 100, 300))
            else:
                draw_card(SCREEN, card, (50 + i * 100, 300))


        # Player has stood, now dealer's turn
        if player_stood:
            dealer_value = dealer_hit()

            # Draw dealer's hand after hitting
            for i, card in enumerate(dealer_hand):
                draw_card(SCREEN, card, (50 + i * 100, 300))

        # Draw buttons with updated text
        pygame.draw.rect(SCREEN, "Black", (600, 400, 100, 50))  # Hit button
        hit_text_surface = get_font(30).render("Hit", True, "White")
        SCREEN.blit(hit_text_surface, (620, 410))

        pygame.draw.rect(SCREEN, "Black", (600, 500, 100, 50))  # Stand button
        stand_text_surface = get_font(30).render("Stand", True, "White")
        SCREEN.blit(stand_text_surface, (610, 510))

        # Draw game information
        text_surface = get_font(45).render("Player Balance: $1000", True, "Black")
        SCREEN.blit(text_surface, (50, 40))
        text_surface = get_font(45).render("Bet Amount: $10", True, "Black")
        SCREEN.blit(text_surface, (50, 85))

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
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()  # Adjust the number of decks as needed
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
