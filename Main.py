
from Game import Game
def main():
    num_decks = int(input("Enter the number of decks to use: "))
    game = Game(num_decks)
    
    while True:
        game.play()
        if input("Play again? Main Class (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
