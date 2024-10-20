import random\n\n# Welcome message\nprint("Welcome to the Guessing Game!")
number_to_guess = random.randint(1, 10)
player_guess = int(input("Guess a number between 1 and 10: "))
if player_guess < number_to_guess:\n    print("Too low!")\nelif player_guess > number_to_guess:\n    print("Too high!")\nelse:\n    print("Congratulations! You guessed it!")
while player_guess != number_to_guess:\n    player_guess = int(input("Try again: "))\n    if player_guess < number_to_guess:\n        print("Too low!")\n    elif player_guess > number_to_guess:\n        print("Too high!")
attempts = 1\nwhile player_guess != number_to_guess:\n    player_guess = int(input("Try again: "))\n    attempts += 1
print(f"Congratulations! You guessed it in {attempts} attempts.")
play_again = input("Do you want to play again? (yes/no): ").lower()
def play_game():\n    number_to_guess = random.randint(1, 10)\n    player_guess = int(input("Guess a number between 1 and 10: "))\n    attempts = 1\n    while player_guess != number_to_guess:\n        player_guess = int(input("Try again: "))\n        attempts += 1
    print(f"Congratulations! You guessed it in {attempts} attempts.")\n\nif __name__ == "__main__":\n    play_game()
while play_again == "yes":\n        play_game()\n        play_again = input("Do you want to play again? (yes/no): ").lower()
