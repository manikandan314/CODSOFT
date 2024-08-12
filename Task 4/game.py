import random

def main():
    print("Rock-Paper-Scissors")
    user_score = 0
    computer_score = 0
    values = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while True:
        print("Select Your Choice: ")
        print("1. Rock\n2. Paper\n3. Scissors\n4. Exit")

        try:
            user = int(input("Enter choice (1/2/3/4): "))
            if user not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user == 4:
            print("\nRound Over")
            print(f"Your Score: {user_score}\nComputer Score: {computer_score}")
            if user_score > computer_score:
                print("You Win Overall")
            elif user_score < computer_score:
                print("Better Luck Next Time")
            else:
                print("It's a Tie!")
            break

        computer = random.choice([1, 2, 3])

        print(f"\nPlayer: {values[user]}\nComputer: {values[computer]}")

        if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            user_score += 1
            print("You win this round!\n")
        elif user == computer:
            print("It's a Tie!\n")
        else:
            computer_score += 1
            print("You lose this round.\n")

        print(f"Your score: {user_score}\nComputer score: {computer_score}\n")

if __name__ == "__main__":
    main()
