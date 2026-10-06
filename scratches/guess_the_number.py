import random

def greet():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    difficulty=input("Choose a difficulty, Type 'easy' or 'hard : ' ")
    return difficulty
def play_game(difficulty_level):
    chosen_number = random.randint(1, 100)
    if difficulty_level=='easy':
        attempts=10
    else:
        attempts=5
    while attempts>0:
        user_guess = int(input('Make a guess:'))
        if user_guess > chosen_number:
            print('Too High')
        elif user_guess < chosen_number:
            print("Too low")
        elif user_guess==chosen_number:
            print(f'You guessed it right and the number is {chosen_number}')
            attempts=0
        attempts-=1
    return True

difficulty_level=greet()
play_game(difficulty_level)