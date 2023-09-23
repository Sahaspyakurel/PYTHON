import random

class RockPaperScissors:
    def __init__(self, user_name, address, phone):
        self.user_name = user_name
        self.address = address
        self.phone = phone

    def computer_random_number_gen(self):
        return random.randint(1, 3)

    def display_computer_choice(self, choice):
        options = {1: "R", 2: "P", 3: "S"}
        return options[choice]

    def display_user_choice(self):
        print("Enter your choice:")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")
        user_choice = int(input("Enter the number of your choice (1/2/3): "))
        while user_choice not in [1, 2, 3]:
            print("Invalid choice. Please try again.")
            user_choice = int(input("Enter the number of your choice (1/2/3): "))
        return user_choice

    def determine_winner(self, user_choice, computer_choice):
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

    def display_static_info(self, winner):
        with open("result.txt", "a") as file:
            if winner == "tie":
                file.write("It's a tie!\n")
            else:
                file.write(f"{winner} has won the game!\n")
                file.write(f"User Information:\n")
                file.write(f"Name: {self.user_name}\n")
                file.write(f"Address: {self.address}\n")
                file.write(f"Phone: {self.phone}\n")

    def play_game(self):
        while True:
            user_choice = self.display_user_choice()
            computer_choice = self.computer_random_number_gen()

            print(f"Computer chose: {self.display_computer_choice(computer_choice)}")

            winner = self.determine_winner(user_choice, computer_choice)
            if winner != "tie":
                self.display_static_info(winner)

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
    user_name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")

    game = RockPaperScissors(user_name, address, phone)
    game.play_game()
