import random
from replit import clear
from art import logo

# This function is used to randomly choose a card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# This function calculates the score of the cards
def score_cards(cards):
    # Check for a blackjack (Ace + 10 = 21) with only two cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If there is an Ace (11) and the total is over 21, convert it to 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# This function compares the user and computer scores
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score > 21:
        return "You went over. You lose 😒"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😍"
    else:
        return "You lose 😪"

# This is the main game function
def play_game():
    print(logo)

    # Creating empty lists for the user and computer cards
    your_cards = []
    computers = []
    is_game_over = False

    # Deal two cards each for user and computer
    for _ in range(2):
        your_cards.append(deal_card())
        computers.append(deal_card())

    # Game loop: runs until the game is over
    while not is_game_over:
        user_score = score_cards(your_cards)
        computer_score = score_cards(computers)
        
        print(f"Your cards: {your_cards}, current score: {user_score}")
        print(f"Computer's first card: {computers[0]}")
        
        # End game if user/computer gets Blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want to draw another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                your_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards while score is less than 17
    while computer_score != 0 and computer_score < 17:
        computers.append(deal_card())
        computer_score = score_cards(computers)

    # Final results
    print(f"Your final hand: {your_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computers}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Ask to replay the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
