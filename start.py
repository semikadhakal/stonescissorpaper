import random

print("******Welcome To Rock Paper Scissors*******")
l = ["rock", "scissor", "paper"]

while True:
    Ccount = 0
    ucount = 0

    print("\nMenu:")
    print("1. Start New Game")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        print(f"Welcome, {name}!\n")

        for _ in range(5):  # Play 5 rounds
            print("Choose your move:")
            print("1. Rock")
            print("2. Scissor")
            print("3. Paper")
            userInput = int(input("Enter your choice (1/2/3): "))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue

            Cchoice = random.choice(l)

            print(f"Computer chose: {Cchoice}")
            print(f"You chose: {uchoice}")

            if Cchoice == uchoice:
                print("It's a draw!")
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("You win!")
                ucount += 1
            else:
                print("Computer wins!")
                Ccount += 1

        print("\nGame Over!")
        print("Final Score:")
        print(f"{name}: {ucount}")
        print("Computer: ", Ccount)

    elif choice == '2':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1 or 2.")
