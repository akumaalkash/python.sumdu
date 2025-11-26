import random # 1. Завантажуємо модуль для випадкових чисел

def start_game():
    secret_number = random.randint(1, 10) # 2. Загадуємо число від 1 до 10
    guessed = False # Змінна-прапорець: гравець ще НЕ вгадав

    print("Let`s start!")

    while not guessed: 

        try:
            guess_text = input ("Guess the number from 1 to 10: ")
            guess = int(guess_text)

            if guess == secret_number:
                print("You are right! The number is", secret_number)
                guessed = True # Змінюємо прапорець, щоб вийти з циклу
            elif guess > secret_number:
                print("Your number is too large!")
            else:
                print("Your number is too small!")
        except ValueError:
            print("Something went wrong. Try fucking nmbers!!!")


    print("The game is finished.")

start_game() 