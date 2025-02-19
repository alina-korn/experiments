def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encode" else -shift
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
mode = input("Шифровать (encode) или расшифровать (decode)? ").lower()
print("Результат:", caesar_cipher(text, shift, mode))
