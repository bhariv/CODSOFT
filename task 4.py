import random


def get_user_choice(valid_choices):
    """Prompt the user until a valid choice is made."""
    while True:
        print("Choose Rock, Paper, or Scissors (rock/paper/scissors): ")
        choice = input(" > ").lower()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please choose again.")



def get_computer_choice(valid_choices):
    """Random pick a choice for the computer."""
    return random.choice(valid_choices)

def decide_winner(user, computer, rules):
    "Determine the winner using predefined game rules."""
    if user == computer:
        return "tie"
    elif rules[user] == computer:
        return "user"
    else:
        return "computer"

def play_game():
    options = ("rock", "paper", "scissors")
    game_rules = {
        "rock": "scissors",
        "paper":"rock",
        "scissors": "paper"
    }

    user_score = 0
    computer_score = 0

    print(" Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice(options)
        computer_choice = get_computer_choice(options)

        print(f"\n You choose: {user_choice}")
        print(f" Computer choose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice, game_rules)

        if result == "tie":
            print("Result: It's a tie!")
        elif result == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print(f" score --- You: {user_score} | Computer: {computer_score}\n")


        replay = input("Do you want to play again? (yes/no: ").lower()
        if replay != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        
play_game()

        
    
