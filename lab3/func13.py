import random

def guess_number():
    lower_bound = 1
    upper_bound = 20
    random_number = random.randint(lower_bound, upper_bound)

    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between {lower_bound} and {upper_bound}.")

    count_attempts = 0

    while True:
        try:
            guess = int(input("Take a guess: "))
            count_attempts += 1

            if guess < random_number:
                print(f"Your guess is too low.")
            elif guess > random_number:
                print(f"Your guess is too high.")
            elif guess == random_number:
                print(f"Good job, {name}! You guessed my number in {count_attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_number()
            