import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    play_game()
