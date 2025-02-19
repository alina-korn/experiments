questions = {
    "Сколько планет в Солнечной системе? ": "8",
    "Какой язык программирования мы используем? ": "python",
    "Столица Франции? ": "париж"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()
    if user_answer == answer:
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно! Правильный ответ: {answer}")

print(f"Ваш результат: {score} из {len(questions)}")
