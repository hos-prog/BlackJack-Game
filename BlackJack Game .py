#Adem Hosama 
#Blackjack game simple project
import random

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []

# Deal two cards to the player
for _ in range(2):
    your_cards.append(random.choice(cards))

# Deal one card to the computer
computer_cards.append(random.choice(cards))

# Ask if the player wants to play
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play_game.lower() == 'y':
    print(f"Your cards: {your_cards}")
    print(f"Computer's first card: {computer_cards}")

    # Ask if the player wants another card
    more_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if more_card.lower() == 'y':
        your_cards.append(random.choice(cards))

    # Computer draws a second card regardless of player choice (to continue the game)
    computer_cards.append(random.choice(cards))

    print(f"Your final hand: {your_cards}, total: {sum(your_cards)}")
    print(f"Computer's final hand: {computer_cards}, total: {sum(computer_cards)}")

    # Determine result
    if sum(your_cards) > 21:
        print("You went over. You lose 😢")
    elif sum(computer_cards) > 21:
        print("Computer went over. You win! 🎉")
    elif sum(your_cards) > sum(computer_cards):
        print("You win 👌")
    elif sum(your_cards) == sum(computer_cards):
        print("Draw the Game!")
    else:
        print("You lose 😢")
else:
    print("Maybe next time!")
