import random

def ComputerRandomNumberGen():
    return random.randint(1, 3)

def displayComputerChoice(choice):
    options = {1: "R", 2: "P", 3: "S"}
    return options[choice]

def displayUserChoice():
    print("Enter your choice:")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    user_choice = int(input("Enter the number of your choice (1/2/3): "))
    while user_choice not in [1, 2, 3]:
        print("Invalid choice. Please try again.")
        user_choice = int(input("Enter the number of your choice (1/2/3): "))
    return user_choice

def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == 1 and computer_choice == 3:
        return "user"
    elif user_choice == 2 and computer_choice == 1:
        return "user"
    elif user_choice == 3 and computer_choice == 2:
        return "user"
    else:
        return "computer"

def display_static_Info(winner, user_name, address, phone):
    with open("result.txt", "a") as file:
        if winner == "tie":
            file.write("It's a tie!\n")
        else:
            file.write(f"{winner} has won the game!\n")
            file.write(f"User Information:\n")
            file.write(f"Name: {user_name}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Phone: {phone}\n")

def main():
    user_name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    while True:
        user_choice = displayUserChoice()
        computer_choice = ComputerRandomNumberGen()

        print(f"Computer chose: {displayComputerChoice(computer_choice)}")

        winner = DetermineWinnerOfRPS(user_choice, computer_choice)
        if winner != "tie":
            display_static_Info(winner, user_name, address, phone)

        if winner == "user":
            print("Congratulations! You won!")
        elif winner == "computer":
            print("Sorry, the computer won.")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
