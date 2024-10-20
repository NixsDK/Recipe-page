import random\n\n# Welcome message\nprint("Welcome to the Guessing Game!")
number_to_guess = random.randint(1, 10)
player_guess = int(input("Guess a number between 1 and 10: "))
if player_guess < number_to_guess:\n    print("Too low!")\nelif player_guess > number_to_guess:\n    print("Too high!")\nelse:\n    print("Congratulations! You guessed it!")
