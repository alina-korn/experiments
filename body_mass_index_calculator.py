def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))
bmi = calculate_bmi(weight, height)
print(f"Ваш ИМТ: {bmi:.2f}")
