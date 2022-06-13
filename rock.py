
user_choice= input("Enter one of(rock, paper, scissors): ")
possible_choice = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choice)
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")
