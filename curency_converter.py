def convert_currency(amount, rate):
    return amount * rate

amount = float(input("Введите сумму: "))
rate = float(input("Введите курс обмена (например, 0.85 для USD to EUR): "))
print(f"Конвертированная сумма: {convert_currency(amount, rate):.2f}")
