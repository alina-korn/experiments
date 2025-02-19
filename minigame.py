import random

choices = ["камень", "ножницы", "бумага"]

def play_game():
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    computer_choice = random.choice(choices)

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

play_game()
