# Лабораторная работа № 5. Вариант 8: «Числа в строке»
# Извлечение всех целых чисел из строки и вычисление их суммы

def main() -> None:
    # Ввод произвольной строки (может быть пустой, содержать буквы и спецсимволы)
    text: str = input("Введите строку: ")

    # Проверка пустой строки или строки только из пробелов
    if not text.strip():
        print("Введена пустая строка. Чисел не найдено, сумма: 0")
        return

    numbers: list[int] = []
    current_digits: str = ""

    # Посимвольный разбор строки с добавлением пробела-разделителя в конце
    for ch in text + " ":
        if ch.isdigit():
            current_digits += ch
        elif current_digits:
            numbers.append(int(current_digits))
            current_digits = ""

    total_sum: int = sum(numbers)

    # Вывод результатов в читаемом виде с пояснениями
    print("\n--- Результаты анализа строки ---")
    print(f"Извлечённые числа: {numbers}")
    print(f"Количество найденных чисел: {len(numbers)}")
    print(f"Сумма всех чисел в строке: {total_sum}")


if __name__ == "__main__":
    main()
