import random

ROCK = "1"
PAPER = "2"
SCISSORS = "3"

CHOICES_MAPPING = {
    ROCK: "Rock",
    PAPER: "Paper",
    SCISSORS: "Scissors"
}

WINNING_COMBINATIONS = {
    (ROCK, SCISSORS),
    (PAPER, ROCK),
    (SCISSORS, PAPER)
}

def print_options():
    print("\nChoices:")
    for choice, label in CHOICES_MAPPING.items():
        print(f"{choice} - {label}")
    print()

def get_user_choice():
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in CHOICES_MAPPING:
            return choice
        print("Invalid choice. Please try again.\n")
        print_options()

def get_computer_choice():
    return str(random.randint(1, 3))

def print_round_result(user_choice, comp_choice, user_score, comp_score):
    user_choice_str = CHOICES_MAPPING[user_choice]
    comp_choice_str = CHOICES_MAPPING[comp_choice]

    print(f"You chose {user_choice_str}")
    print(f"Computer chose {comp_choice_str}")

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice, comp_choice) in WINNING_COMBINATIONS:
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1

    print(f"Score: You {user_score}, Computer {comp_score}\n")
    return user_score, comp_score

def print_final_result(user_score, comp_score):
    if user_score > comp_score:
        print("Congratulations! You win!")
    elif user_score < comp_score:
        print("Sorry, computer wins. Better luck next time.")
    else:
        print("It's a tie!")

print("Rock Paper Scissors\n")

rounds = int(input("Best out of how many rounds? "))
print_options()

user_score = 0
comp_score = 0

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    user_score, comp_score = print_round_result(user_choice, comp_choice, user_score, comp_score)

print_final_result(user_score, comp_score)
