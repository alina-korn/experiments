import random

number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Твоя догадка: "))
    attempts += 1

    if guess < number:
        print("Больше!")
    elif guess > number:
        print("Меньше!")
    else:
        print(f"Поздравляю! Вы угадали число за {attempts} попыток.")
        break
