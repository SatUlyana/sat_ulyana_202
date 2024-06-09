import random
import string


def generate_password(length, use_digits, use_symbols, use_uppercase):
    marks = string.ascii_lowercase
    if use_digits.lower() == "да":
        marks += string.digits
    if use_symbols.lower() == "да":
        marks += string.punctuation
    if use_uppercase.lower() == "да":
        marks += string.ascii_uppercase

    password = ''.join(random.choice(marks) for _ in range(length))
    return password


length = int(input("Укажите длину пароля: "))
use_digits = input("Использовать цифры (да/нет): ")
use_symbols = input("Использовать символы (да/нет): ")
use_uppercase = input("Использовать заглавные буквы (да/нет): ")


password = generate_password(length, use_digits, use_symbols, use_uppercase)

print(f"Сгенерированный пароль: {password}")